// Gate v2 packaging (MATH3us.md §1.7, E9): automates the release bundle.
// Self-containment is invariant since v0; this tool automates producing
// the single-file release artifact and recording its identity.
//
// Inlines any local <script src> / <link rel=stylesheet href> that point
// inside the chapter directory (lib/ is allowed during development), then
// writes the bundle to releases/bundles/<chapter>.html (regenerable,
// gitignored) and the identity report to <chapter>/audit/bundle-report.json
// (committed). A chapter whose index.html is already self-contained
// produces a byte-identical bundle; the report records that.
//
// Usage: node tools/bundle.mjs caps/03-quatro
import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'fs';
import { resolve, dirname, basename, join } from 'path';
import { createHash } from 'crypto';
import { execSync } from 'child_process';

const chapterDir = resolve(process.argv[2] ?? '');
if (!existsSync(join(chapterDir, 'index.html'))) {
  console.error(`FAIL no index.html in ${chapterDir}`);
  process.exit(1);
}

const source = readFileSync(join(chapterDir, 'index.html'), 'utf8');
const inlined = [];
const unresolved = [];

// local <script src="..."></script> → inline body
let html = source.replace(
  /<script([^>]*)\ssrc=["']([^"':]+)["']([^>]*)>\s*<\/script>/g,
  (m, pre, src, post) => {
    const p = resolve(chapterDir, src);
    if (!p.startsWith(chapterDir) || !existsSync(p)) { unresolved.push(src); return m; }
    inlined.push(src);
    return `<script${pre}${post}>\n${readFileSync(p, 'utf8')}\n</script>`;
  });

// local <link rel="stylesheet" href="..."> → inline <style>
html = html.replace(
  /<link([^>]*)\srel=["']stylesheet["']([^>]*)\shref=["']([^"':]+)["']([^>]*)\/?>/g,
  (m, a, b, href, c) => {
    const p = resolve(chapterDir, href);
    if (!p.startsWith(chapterDir) || !existsSync(p)) { unresolved.push(href); return m; }
    inlined.push(href);
    return `<style>\n${readFileSync(p, 'utf8')}\n</style>`;
  });

const bundleDir = resolve('releases/bundles');
mkdirSync(bundleDir, { recursive: true });
const bundlePath = join(bundleDir, basename(chapterDir) + '.html');
writeFileSync(bundlePath, html);

const sha = h => createHash('sha256').update(h).digest('hex');
const report = {
  chapter_dir: basename(chapterDir),
  script: 'tools/bundle.mjs',
  gate: 'v2',
  code_commit: execSync('git rev-parse --short HEAD').toString().trim(),
  date: new Date().toISOString().slice(0, 10),
  bundle_path: 'releases/bundles/' + basename(chapterDir) + '.html',
  bundle_sha256: sha(html),
  source_sha256: sha(source),
  already_self_contained: html === source,
  inlined_local_refs: inlined,
  unresolved_local_refs: unresolved,
};
mkdirSync(join(chapterDir, 'audit'), { recursive: true });
writeFileSync(join(chapterDir, 'audit', 'bundle-report.json'),
  JSON.stringify(report, null, 2) + '\n');

const ok = unresolved.length === 0;
console.log(`${ok ? 'ok  ' : 'FAIL'} bundle ${basename(chapterDir)} — ` +
  (report.already_self_contained
    ? 'already self-contained (bundle byte-identical)'
    : `${inlined.length} local ref(s) inlined`) +
  (ok ? '' : `; UNRESOLVED: ${unresolved.join(', ')}`));
process.exit(ok ? 0 : 1);
