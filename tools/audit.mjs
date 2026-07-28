// Gate v0 audit for a chapter page (MATH3us.md §1.7).
// Screenshots (desktop + iPhone viewport), basic interaction test,
// overflow/clipping/canvas/formula/typography inspection, network
// self-containment check. Writes artifacts into <chapter>/audit/.
//
// Usage: node tools/audit.mjs caps/01-exaustao
// Playwright is resolved via NODE_PATH (dev dependency, not vendored);
// the browser executable comes from PW_CHROMIUM or the environment default.
import { createRequire } from 'module';
import { existsSync, writeFileSync } from 'fs';
import { resolve } from 'path';
import { execSync } from 'child_process';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');

const chapterDir = resolve(process.argv[2] ?? 'caps/01-exaustao');
const pageUrl = 'file://' + chapterDir + '/index.html';
const auditDir = chapterDir + '/audit';

const exePath = process.env.PW_CHROMIUM
  ?? (existsSync('/opt/pw-browsers/chromium') ? '/opt/pw-browsers/chromium' : undefined);

const report = {
  chapter_dir: chapterDir,
  script: 'tools/audit.mjs',
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

  // -- interaction: double 4x (6 -> 96), verify status against recurrences
  for (let i = 0; i < 4; i++) await page.click('#btn-doble');
  const status96 = await page.textContent('#leitura');
  // independent expectation computed here (same algorithm, separate run)
  let a = 3, b = 2 * Math.sqrt(3);
  for (let i = 0; i < 4; i++) { b = 2 * a * b / (a + b); a = Math.sqrt(a * b); }
  const wantA = a.toFixed(8).replace('.', ','), wantB = b.toFixed(8).replace('.', ',');
  check(`${name}.interaction_values_n96`,
    status96.includes('n = 96') && status96.includes(wantA) && status96.includes(wantB),
    `expected a=${wantA} b=${wantB} in "${status96.slice(0, 80)}…"`);

  // -- back / reset round trip
  await page.click('#btn-back');
  const back = await page.textContent('#leitura');
  await page.click('#btn-reset');
  const reset = await page.textContent('#leitura');
  check(`${name}.back_and_reset`, back.includes('n = 48') && reset.includes('n = 6'));

  // -- keyboard operability: focus button, activate with Enter
  await page.focus('#btn-doble');
  await page.keyboard.press('Enter');
  const afterEnter = await page.textContent('#leitura');
  check(`${name}.keyboard_activation`, afterEnter.includes('n = 12'));

  // -- zoom slider responds to input events
  await page.fill('#zoom', '120');
  await page.dispatchEvent('#zoom', 'input');
  const zoomLabel = await page.textContent('#zoom-val');
  check(`${name}.zoom_control`, zoomLabel.trim() === '120×');

  // -- overflow / clipping
  const overflow = await page.evaluate(() =>
    document.documentElement.scrollWidth > document.documentElement.clientWidth);
  check(`${name}.no_horizontal_overflow`, !overflow);

  // -- canvases: labeled, sized, actually painted (non-blank pixel share)
  const canvasInfo = await page.evaluate(() => {
    return [...document.querySelectorAll('canvas')].map(c => {
      const ctx = c.getContext('2d');
      const d = ctx.getImageData(0, 0, c.width, c.height).data;
      let painted = 0;
      for (let i = 0; i < d.length; i += 40) if (d[i + 3] !== 0) painted++;
      return { label: c.getAttribute('aria-label') ?? '', w: c.width, h: c.height,
               paintedShare: painted / (d.length / 40) };
    });
  });
  check(`${name}.canvases_labeled_and_painted`,
    canvasInfo.length === 3 && canvasInfo.every(c => c.label.length > 20 && c.paintedShare > 0.001),
    canvasInfo.map(c => c.paintedShare.toFixed(4)).join(', '));

  // -- double-siege lab (section 7, rebuild D3): tables mirror state,
  //    inheritance visible in DOM, plot painted in both modes
  const siege = await page.evaluate(() => ({
    areasRows: document.querySelectorAll('#tabela-areas-corpo tr').length,
    normRows: document.querySelectorAll('#tabela-normal-corpo tr').length,
    firstAin: document.querySelector('#tabela-areas-corpo tr:nth-child(2) td:nth-child(2)')?.textContent,
    firstA: document.querySelector('#tabela-corpo tr:nth-child(1) td:nth-child(2)')?.textContent,
  }));
  check(`${name}.areas_table_mirrors_state`, siege.areasRows === 2, `rows=${siege.areasRows}`);
  check(`${name}.normalized_table_full_range`, siege.normRows === 17, `rows=${siege.normRows}`);
  check(`${name}.inheritance_visible_in_tables`, siege.firstAin === siege.firstA,
    `A-_{2n} cell "${siege.firstAin}" vs a_n cell "${siege.firstA}" (Enunciado F)`);
  const plotPainted = () => page.evaluate(() => {
    const c = document.getElementById('cv-plot');
    const d = c.getContext('2d').getImageData(0, 0, c.width, c.height).data;
    let p = 0;
    for (let i = 3; i < d.length; i += 4) if (d[i] !== 0) p++;
    return p / (d.length / 4);
  });
  const pv = await plotPainted();
  await page.click('#btn-plot-errs');
  const pe = await plotPainted();
  await page.click('#btn-plot-vals');
  check(`${name}.plot_painted_both_modes`, pv > 0.001 && pe > 0.001,
    `vals: ${pv.toFixed(4)}, errs: ${pe.toFixed(4)}`);

  // -- formulas are text (no images), live region present, table has data
  const dom = await page.evaluate(() => ({
    formulaCount: document.querySelectorAll('.formula').length,
    imgCount: document.querySelectorAll('img').length,
    liveRegion: !!document.querySelector('[aria-live]'),
    tableRows: document.querySelectorAll('#tabela-corpo tr').length,
    exCount: document.querySelectorAll('.exercicio').length,
    gabCount: document.querySelectorAll('details.gab').length,
  }));
  check(`${name}.formulas_textual_no_images`, dom.formulaCount >= 8 && dom.imgCount === 0);
  check(`${name}.aria_live_region_present`, dom.liveRegion);
  check(`${name}.table_mirrors_state`, dom.tableRows === 2, `rows=${dom.tableRows} (after reset+1 doubling)`);

  // -- exercises (E20): present in tiers, every one with a details/summary
  check(`${name}.exercises_with_gabaritos`, dom.exCount >= 12 && dom.gabCount >= dom.exCount,
    `exercicios=${dom.exCount}, gabaritos=${dom.gabCount}`);
  await page.click('details.gab summary >> nth=0');
  const gabOpens = await page.evaluate(() => document.querySelector('details.gab').open);
  await page.click('details.gab summary >> nth=0');
  check(`${name}.gabarito_keyboard_toggle`, gabOpens);

  // -- self-containment: zero non-file requests
  check(`${name}.self_contained_no_network`, external.length === 0,
    external.length ? external.join(' ') : 'only file:// requests');

  // -- magnifier must never go blank across the zoom range
  //    (render incident 2026-07-28: iOS arc rasterization + field framing)
  // NOTE: read EVERY pixel. A sparse stride aliases against the thin
  // near-vertical traces (stride-40 sampling lands only on columns
  // divisible by 20 and can miss all three lines entirely) — a pure
  // observation-layer artifact that produced a false "blank" on the
  // first run of this invariant.
  const lupaPainted = () => page.evaluate(() => {
    const c = document.getElementById('cv-zoom');
    const d = c.getContext('2d').getImageData(0, 0, c.width, c.height).data;
    let p = 0;
    for (let i = 3; i < d.length; i += 4) if (d[i] !== 0) p++;
    return p / (d.length / 4);
  });
  await page.click('#btn-reset');
  await page.fill('#zoom', '400'); await page.dispatchEvent('#zoom', 'input');
  const paintedN6 = await lupaPainted();
  for (let i = 0; i < 4; i++) await page.click('#btn-doble');
  const paintedN96 = await lupaPainted();
  check(`${name}.magnifier_painted_at_extreme_zoom`,
    paintedN6 > 0.0005 && paintedN96 > 0.0005,
    `share n=6: ${paintedN6.toFixed(4)}, n=96: ${paintedN96.toFixed(4)} at 400x`);
  await page.click('#btn-reset'); await page.click('#btn-doble');
  await page.fill('#zoom', '120'); await page.dispatchEvent('#zoom', 'input');

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
