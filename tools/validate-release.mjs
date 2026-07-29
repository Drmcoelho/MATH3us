// Gate v2 release validation (MATH3us.md §1.7, E9): automates the
// self-containment check that was manual in v0/v1. Two legs:
//
// 1. Static: the bundle (releases/bundles/<chapter>.html, produced by
//    bundle.mjs; falls back to the chapter index.html with a warning)
//    must not load any remote resource — script/link/img/iframe/source
//    src|href, url(...), @import, fetch(, XMLHttpRequest, WebSocket,
//    dynamic import( pointing at http(s):// or protocol-relative //.
//    Plain <a href="http…"> navigation links are reported, not failed:
//    the page must *function* without network; leaving it may use one.
// 2. Dynamic: load the bundle over file:// in Chromium and fail on any
//    non-file:// request, console error or page error; require a
//    non-trivially painted document.
//
// Writes <chapter>/audit/release-validation.json. Exit 0 only if valid.
//
// Usage: node tools/validate-release.mjs caps/03-quatro
import { createRequire } from 'module';
import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'fs';
import { resolve, join, basename } from 'path';
import { execSync } from 'child_process';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');

const chapterDir = resolve(process.argv[2] ?? '');
const bundlePath = resolve('releases/bundles', basename(chapterDir) + '.html');
const usingBundle = existsSync(bundlePath);
const target = usingBundle ? bundlePath : join(chapterDir, 'index.html');
const html = readFileSync(target, 'utf8');

const report = {
  chapter_dir: basename(chapterDir),
  script: 'tools/validate-release.mjs',
  gate: 'v2',
  code_commit: execSync('git rev-parse --short HEAD').toString().trim(),
  date: new Date().toISOString().slice(0, 10),
  validated_file: usingBundle ? report_rel(bundlePath) : report_rel(target),
  bundle_used: usingBundle,
  checks: {},
  navigation_links: [],
  violations: [],
};
function report_rel(p) { return p.replace(resolve('.') + '/', ''); }
const check = (name, passed, detail) => {
  report.checks[name] = { passed, ...(detail ? { detail } : {}) };
  console.log(`${passed ? 'ok  ' : 'FAIL'} ${name}${detail ? ' — ' + detail : ''}`);
};

// -- static leg
const remote = /(?:https?:)?\/\/[^\s"'<>)]+/g;
const loaders = [
  [/<(?:script|img|iframe|source|video|audio|embed|track)[^>]*\ssrc=["']((?:https?:)?\/\/[^"']+)["']/gi, 'src'],
  [/url\(\s*["']?((?:https?:)?\/\/[^"')]+)["']?\s*\)/gi, 'css url()'],
  [/@import\s+["']((?:https?:)?\/\/[^"']+)["']/gi, '@import'],
  [/\bfetch\(\s*["']((?:https?:)?\/\/[^"']+)["']/gi, 'fetch'],
  [/\bnew\s+WebSocket\(\s*["']([^"']+)["']/gi, 'WebSocket'],
  [/\bimport\(\s*["']((?:https?:)?\/\/[^"']+)["']/gi, 'dynamic import'],
  [/XMLHttpRequest/g, 'XMLHttpRequest (presence)'],
];
for (const [re, kind] of loaders) {
  for (const m of html.matchAll(re)) {
    report.violations.push({ kind, ref: (m[1] ?? m[0]).slice(0, 200) });
  }
}
// <link> tags: only rels that trigger a fetch are violations. Pure-metadata
// rels (canonical, alternate, license) declare facts about the page and load
// nothing — the dynamic zero_network_requests leg is the proof either way.
// A remote href with a loading rel, an unknown rel, or no rel at all still fails.
const METADATA_RELS = new Set(['canonical', 'alternate', 'license']);
for (const m of html.matchAll(/<link\b[^>]*>/gi)) {
  const tag = m[0];
  const href = tag.match(/\shref=["']((?:https?:)?\/\/[^"']+)["']/i);
  if (!href) continue;
  const rels = (tag.match(/\srel=["']([^"']+)["']/i)?.[1] ?? '')
    .trim().toLowerCase().split(/\s+/).filter(Boolean);
  const metadataOnly = rels.length > 0 && rels.every(r => METADATA_RELS.has(r));
  if (!metadataOnly) report.violations.push({ kind: 'link href', ref: href[1].slice(0, 200) });
}
for (const m of html.matchAll(/<a[^>]*\shref=["'](https?:\/\/[^"']+)["']/gi)) {
  report.navigation_links.push(m[1].slice(0, 200));
}
check('static.no_remote_resource_loads', report.violations.length === 0,
  report.violations.length ? JSON.stringify(report.violations.slice(0, 5)) : undefined);

// -- dynamic leg
const exePath = process.env.PW_CHROMIUM
  ?? (existsSync('/opt/pw-browsers/chromium') ? '/opt/pw-browsers/chromium' : undefined);
const browser = await chromium.launch({ executablePath: exePath });
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
const externalReqs = [];
const errors = [];
page.on('request', r => { if (!r.url().startsWith('file://')) externalReqs.push(r.url()); });
page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
page.on('pageerror', e => errors.push(e.message));
await page.goto('file://' + target, { waitUntil: 'load' });
await page.waitForTimeout(1200);

check('dynamic.zero_network_requests', externalReqs.length === 0,
  externalReqs.length ? externalReqs.slice(0, 3).join(' ') : undefined);
check('dynamic.zero_console_or_page_errors', errors.length === 0,
  errors.length ? errors.slice(0, 3).join(' | ') : undefined);
const textLen = (await page.evaluate(() => document.body?.innerText.length ?? 0));
check('dynamic.document_painted', textLen > 500, `body text length ${textLen}`);
await browser.close();

report.external_requests = externalReqs;
report.errors = errors;
mkdirSync(join(chapterDir, 'audit'), { recursive: true });
writeFileSync(join(chapterDir, 'audit', 'release-validation.json'),
  JSON.stringify(report, null, 2) + '\n');

const allPassed = Object.values(report.checks).every(c => c.passed);
console.log(`${allPassed ? 'ok  ' : 'FAIL'} ${basename(chapterDir)} release validation ` +
  `(${report.navigation_links.length} navigation link(s) noted, not failed)`);
process.exit(allPassed ? 0 : 1);
