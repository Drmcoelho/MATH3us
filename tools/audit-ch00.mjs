// Gate v0 audit for chapter 0 (A Inferencia) — MATH3us.md §1.7.
// Screenshots (desktop + iPhone viewport), interaction test of both labs,
// overflow/clipping/canvas/formula inspection, network self-containment.
// Writes artifacts into caps/00-inferencia/audit/.
//
// Usage: node tools/audit-ch00.mjs
// Playwright is resolved via NODE_PATH (dev dependency, not vendored);
// the browser executable comes from PW_CHROMIUM or the environment default.
import { createRequire } from 'module';
import { existsSync, writeFileSync } from 'fs';
import { resolve } from 'path';
import { execSync } from 'child_process';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');

const chapterDir = resolve(process.argv[2] ?? 'caps/00-inferencia');
const pageUrl = 'file://' + chapterDir + '/index.html';
const auditDir = chapterDir + '/audit';

const exePath = process.env.PW_CHROMIUM
  ?? (existsSync('/opt/pw-browsers/chromium') ? '/opt/pw-browsers/chromium' : undefined);

const report = {
  chapter_dir: chapterDir,
  script: 'tools/audit-ch00.mjs',
  code_commit: execSync('git rev-parse --short HEAD').toString().trim(),
  date: new Date().toISOString().slice(0, 10),
  gate: 'v0',
  checks: {},
  errors: [],
};
const check = (name, passed, detail) => {
  report.checks[name] = { passed, ...(detail ? { detail } : {}) };
  console.log(`${passed ? 'ok  ' : 'FAIL'} ${name}${detail ? ' — ' + detail : ''}`);
};

const browser = await chromium.launch({ executablePath: exePath });

async function auditViewport(name, viewport) {
  const page = await browser.newPage({ viewport });
  const external = [];
  page.on('request', r => { if (!r.url().startsWith('file://')) external.push(r.url()); });
  page.on('console', m => { if (m.type() === 'error') report.errors.push(`[${name}] ${m.text()}`); });
  page.on('pageerror', e => report.errors.push(`[${name}] ${e.message}`));
  await page.goto(pageUrl);

  // -- lab 1: walk n to 96 via slider, verify status against an
  //    independent expectation computed here (separate run of the math)
  await page.fill('#n-range', '96');
  await page.dispatchEvent('#n-range', 'input');
  const status96 = await page.textContent('#leitura-1');
  const rho96 = Math.cos(Math.PI / 96).toFixed(10).replace('.', ',');
  const def96 = (2 * Math.sin(Math.PI / 192) ** 2).toFixed(10).replace('.', ',');
  check(`${name}.lab1_values_n96`,
    status96.includes('n = 96') && status96.includes(rho96) && status96.includes(def96),
    `expected rho=${rho96}, deficit=${def96} in "${status96.slice(0, 90)}…"`);

  // -- buttons: minus / plus / double / reset round trip
  await page.click('#btn-reset');
  await page.click('#btn-plus');
  const s4 = await page.textContent('#leitura-1');
  await page.click('#btn-double');
  const s8 = await page.textContent('#leitura-1');
  await page.click('#btn-minus');
  const s7 = await page.textContent('#leitura-1');
  check(`${name}.lab1_buttons`,
    s4.includes('n = 4') && s8.includes('n = 8') && s7.includes('n = 7'));

  // -- keyboard operability: focus button, activate with Enter
  await page.click('#btn-reset');
  await page.focus('#btn-plus');
  await page.keyboard.press('Enter');
  const afterEnter = await page.textContent('#leitura-1');
  check(`${name}.keyboard_activation`, afterEnter.includes('n = 4'));

  // -- lab 2 verdicts: unique / sliver / deviated-ambiguous / circle-not-excluded
  const verdict = () => page.textContent('#lab-veredito');
  await page.fill('#lab-n', '12'); await page.dispatchEvent('#lab-n', 'input');
  const v12 = await verdict();
  check(`${name}.lab2_unique_guaranteed`,
    v12.includes('IDENTIFICAÇÃO UNÍVOCA') && v12.includes('m = 12') && v12.includes('garantia de identificação SIM'),
    v12.slice(0, 120));
  await page.click('.lab-preset[data-n="170"]');
  const v170 = await verdict();
  check(`${name}.lab2_sliver_at_170`,
    v170.includes('m = 170') && v170.includes('fresta'),
    v170.slice(0, 160));
  await page.click('.lab-preset[data-n="171"]');
  await page.fill('#lab-dev', '100'); await page.dispatchEvent('#lab-dev', 'input');
  const v171 = await verdict();
  check(`${name}.lab2_ambiguous_at_171_deviated`,
    v171.includes('AMBÍGUO') && v171.includes('Círculo excluído') && v171.includes('ambiguidade construtível SIM'),
    v171.slice(0, 160));
  await page.fill('#lab-dev', '0'); await page.dispatchEvent('#lab-dev', 'input');
  await page.click('.lab-preset[data-n="100000"]');
  const vBig = await verdict();
  check(`${name}.lab2_circle_not_excluded`,
    vBig.includes('CÍRCULO NÃO É EXCLUÍDO'),
    vBig.slice(0, 140));

  // -- precision slider responds
  await page.fill('#lab-p', '2'); await page.dispatchEvent('#lab-p', 'input');
  const pLabel = await page.textContent('#lab-p-val');
  check(`${name}.lab2_precision_control`, pLabel.trim() === '2');
  await page.fill('#lab-p', '6'); await page.dispatchEvent('#lab-p', 'input');

  // -- overflow / clipping
  const overflow = await page.evaluate(() =>
    document.documentElement.scrollWidth > document.documentElement.clientWidth);
  check(`${name}.no_horizontal_overflow`, !overflow);

  // -- canvases: labeled, painted (read EVERY pixel — the chapter-1 audit's
  //    aliasing lesson: sparse strides miss thin traces)
  const canvasInfo = await page.evaluate(() =>
    [...document.querySelectorAll('canvas')].map(c => {
      const d = c.getContext('2d').getImageData(0, 0, c.width, c.height).data;
      let painted = 0;
      for (let i = 3; i < d.length; i += 4) if (d[i] !== 0) painted++;
      return { label: c.getAttribute('aria-label') ?? '', paintedShare: painted / (d.length / 4) };
    }));
  check(`${name}.canvases_labeled_and_painted`,
    canvasInfo.length === 2 && canvasInfo.every(c => c.label.length > 20 && c.paintedShare > 0.001),
    canvasInfo.map(c => c.paintedShare.toFixed(4)).join(', '));

  // -- wedge canvas still painted at the thin extreme (n = 96)
  await page.fill('#n-range', '96'); await page.dispatchEvent('#n-range', 'input');
  const wedgePainted = await page.evaluate(() => {
    const c = document.getElementById('cv-wedge');
    const d = c.getContext('2d').getImageData(0, 0, c.width, c.height).data;
    let p = 0;
    for (let i = 3; i < d.length; i += 4) if (d[i] !== 0) p++;
    return p / (d.length / 4);
  });
  check(`${name}.wedge_painted_at_n96`, wedgePainted > 0.001,
    `painted share ${wedgePainted.toFixed(4)}`);
  await page.click('#btn-reset');

  // -- formulas are text (no images), live regions present, tables populated
  const dom = await page.evaluate(() => ({
    formulaCount: document.querySelectorAll('.formula').length,
    imgCount: document.querySelectorAll('img').length,
    liveRegions: document.querySelectorAll('[aria-live]').length,
    tableRows: document.querySelectorAll('#tabela-corpo tr').length,
    collapseRows: document.querySelectorAll('#tabela-colapso-corpo tr').length,
  }));
  check(`${name}.formulas_textual_no_images`, dom.formulaCount >= 10 && dom.imgCount === 0,
    `formulas=${dom.formulaCount}, imgs=${dom.imgCount}`);
  check(`${name}.aria_live_regions_present`, dom.liveRegions >= 3, `count=${dom.liveRegions}`);
  check(`${name}.tables_populated`, dom.tableRows === 22 && dom.collapseRows === 5,
    `main=${dom.tableRows}, collapse=${dom.collapseRows}`);

  // -- self-containment: zero non-file requests
  check(`${name}.self_contained_no_network`, external.length === 0,
    external.length ? external.join(' ') : 'only file:// requests');

  // -- screenshot (full page: typography and formulas inspectable)
  await page.screenshot({ path: `${auditDir}/${name}.png`, fullPage: true });
  await page.close();
}

await auditViewport('desktop', { width: 1440, height: 900 });
await auditViewport('iphone', { width: 390, height: 844 });
await browser.close();

check('no_console_or_page_errors', report.errors.length === 0,
  report.errors.join(' | ') || undefined);

report.all_passed = Object.values(report.checks).every(c => c.passed);
writeFileSync(`${auditDir}/interaction-report.json`, JSON.stringify(report, null, 2) + '\n');
console.log(`\n${report.all_passed ? 'AUDIT PASSED' : 'AUDIT FAILED'} — artifacts in ${auditDir}/`);
process.exit(report.all_passed ? 0 : 1);
