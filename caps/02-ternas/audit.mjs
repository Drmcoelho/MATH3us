// Gate v0 audit for Chapter 2 (caps/02-ternas), MATH3us.md §1.7.
// Adapted from tools/audit.mjs for this chapter's control IDs.
// Screenshots (desktop + iPhone viewport), interaction test against an
// independent in-test computation, keyboard operability, overflow /
// canvas / formula inspection, network self-containment check.
// Writes artifacts into caps/02-ternas/audit/.
//
// Usage:
//   NODE_PATH=<scratchpad>/node_modules node caps/02-ternas/audit.mjs
import { createRequire } from 'module';
import { existsSync, writeFileSync } from 'fs';
import { dirname, resolve } from 'path';
import { fileURLToPath } from 'url';
import { execSync } from 'child_process';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');

const chapterDir = dirname(fileURLToPath(import.meta.url));
const pageUrl = 'file://' + resolve(chapterDir, 'index.html');
const auditDir = resolve(chapterDir, 'audit');

const exePath = process.env.PW_CHROMIUM
  ?? (existsSync('/opt/pw-browsers/chromium') ? '/opt/pw-browsers/chromium' : undefined);

const report = {
  chapter_dir: chapterDir,
  script: 'caps/02-ternas/audit.mjs',
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

// independent expectation for the family (computed here, not by the page)
function famExpect(n) {
  const L = (n * n - 1) / 2, R = (n * n + 1) / 2;
  return { n, L, R, P: n * (n + 1), s: n * (n + 1) / 2, K: n * L / 2,
           r: (n - 1) / 2, rn: (n + 1) / 2 };
}

const browser = await chromium.launch({ executablePath: exePath });

async function auditViewport(name, viewport) {
  const page = await browser.newPage({ viewport });
  const external = [];
  page.on('request', r => { if (!r.url().startsWith('file://')) external.push(r.url()); });
  page.on('console', m => { if (m.type() === 'error') report.errors.push(`[${name}] ${m.text()}`); });
  page.on('pageerror', e => report.errors.push(`[${name}] ${e.message}`));
  await page.goto(pageUrl);

  // -- interaction: advance 4x (3 -> 11), verify status against famExpect
  for (let i = 0; i < 4; i++) await page.click('#btn-next');
  const st11 = await page.textContent('#leitura');
  const e11 = famExpect(11);
  check(`${name}.interaction_values_n11`,
    st11.includes('n = 11') && st11.includes('L = ' + e11.L) &&
    st11.includes('R = ' + e11.R) && st11.includes('teste n²+L²−R² = 0') &&
    st11.includes('K = ' + e11.K) && st11.includes('r = ' + e11.r) &&
    st11.includes('rₙ = ' + e11.rn),
    `expected L=${e11.L} R=${e11.R} K=${e11.K} in "${st11.slice(0, 90)}…"`);

  // -- prev / reset round trip
  await page.click('#btn-prev');
  const back = await page.textContent('#leitura');
  await page.click('#btn-reset');
  const reset = await page.textContent('#leitura');
  check(`${name}.prev_and_reset`,
    back.includes('n = 9') && back.includes('L = 40') &&
    reset.includes('n = 3') && reset.includes('L = 4'));

  // -- keyboard operability: focus button, activate with Enter
  await page.focus('#btn-next');
  await page.keyboard.press('Enter');
  const afterEnter = await page.textContent('#leitura');
  check(`${name}.keyboard_activation`, afterEnter.includes('n = 5') && afterEnter.includes('L = 12'));

  // -- slider responds to input events, and status follows
  await page.fill('#n-slider', '17');
  await page.dispatchEvent('#n-slider', 'input');
  const st17 = await page.textContent('#leitura');
  const nVal = await page.textContent('#n-val');
  check(`${name}.slider_control`,
    nVal.trim() === '17' && st17.includes('n = 17') && st17.includes('L = 144') && st17.includes('R = 145'));

  // -- table exists, mirrors the family, highlights current row
  const table = await page.evaluate(() => {
    const rows = [...document.querySelectorAll('#tabela-corpo tr')];
    const cur = document.querySelector('#tabela-corpo tr.atual');
    return { count: rows.length,
             curN: cur ? cur.dataset.n : null,
             firstCells: rows.length ? [...rows[0].children].map(td => td.textContent) : [] };
  });
  check(`${name}.table_rows_and_highlight`,
    table.count === 10 && table.curN === '17' &&
    table.firstCells.slice(0, 4).join(',') === '3,4,5,0',
    `rows=${table.count}, highlighted n=${table.curN}`);

  // -- overflow / clipping
  const overflow = await page.evaluate(() =>
    document.documentElement.scrollWidth > document.documentElement.clientWidth);
  check(`${name}.no_horizontal_overflow`, !overflow);

  // -- canvases: labeled, actually painted. Read EVERY pixel — sparse
  //    stride sampling aliases against thin lines (Chapter 1 incident).
  const canvasInfo = await page.evaluate(() => {
    return [...document.querySelectorAll('canvas')].map(c => {
      const d = c.getContext('2d').getImageData(0, 0, c.width, c.height).data;
      let painted = 0;
      for (let i = 3; i < d.length; i += 4) if (d[i] !== 0) painted++;
      return { label: c.getAttribute('aria-label') ?? '', w: c.width, h: c.height,
               paintedShare: painted / (d.length / 4) };
    });
  });
  check(`${name}.canvases_labeled_and_painted`,
    canvasInfo.length === 2 && canvasInfo.every(c => c.label.length > 20 && c.paintedShare > 0.001),
    canvasInfo.map(c => c.paintedShare.toFixed(4)).join(', '));

  // -- both canvases repaint across the whole n range without going blank
  let alwaysPainted = true;
  for (const nv of ['3', '9', '15', '21']) {
    await page.fill('#n-slider', nv);
    await page.dispatchEvent('#n-slider', 'input');
    const shares = await page.evaluate(() =>
      [...document.querySelectorAll('canvas')].map(c => {
        const d = c.getContext('2d').getImageData(0, 0, c.width, c.height).data;
        let p = 0;
        for (let i = 3; i < d.length; i += 4) if (d[i] !== 0) p++;
        return p / (d.length / 4);
      }));
    if (!shares.every(s => s > 0.001)) alwaysPainted = false;
  }
  check(`${name}.canvases_never_blank_across_range`, alwaysPainted);

  // -- formulas are text (no images), live region present
  const dom = await page.evaluate(() => ({
    formulaCount: document.querySelectorAll('.formula').length,
    imgCount: document.querySelectorAll('img').length,
    liveRegion: !!document.querySelector('[aria-live]'),
    exCount: document.querySelectorAll('.exercicio').length,
    gabCount: document.querySelectorAll('details.gab').length,
    anchors: ['demonstracao-direta', 'reciproca', 'primitividade',
              'estrutura-modular', 'medidas', 'geometria-interna',
              'leitura-euclidiana', 'sintese-consecutivos', 'exercicios']
      .filter(id => !document.getElementById(id)),
  }));
  check(`${name}.formulas_textual_no_images`, dom.formulaCount >= 8 && dom.imgCount === 0,
    `formulas=${dom.formulaCount}, imgs=${dom.imgCount}`);
  check(`${name}.aria_live_region_present`, dom.liveRegion);
  check(`${name}.claims_proof_anchors_exist`, dom.anchors.length === 0,
    dom.anchors.length ? 'missing: ' + dom.anchors.join(',') : 'all 9 anchors present');

  // -- exercises (E20): >= 13 in five tiers, each with a details/summary
  check(`${name}.exercises_with_gabaritos`, dom.exCount >= 13 && dom.gabCount >= dom.exCount,
    `exercicios=${dom.exCount}, gabaritos=${dom.gabCount}`);
  await page.click('details.gab summary >> nth=0');
  const gabOpens = await page.evaluate(() => document.querySelector('details.gab').open);
  await page.click('details.gab summary >> nth=0');
  check(`${name}.gabarito_toggle`, gabOpens);

  // -- self-containment: zero non-file requests
  check(`${name}.self_contained_no_network`, external.length === 0,
    external.length ? external.join(' ') : 'only file:// requests');

  // -- screenshot (full page: typography and formulas inspectable)
  await page.click('#btn-reset');
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
