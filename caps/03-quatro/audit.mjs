// Gate v0 audit for Chapter 3 (MATH3us.md §1.7), adapted from tools/audit.mjs
// to this chapter's control IDs (#probe, #xmax, #btn-left/right/reset).
// Screenshots (desktop + iPhone viewport), interaction test against an
// independent computation, overflow/canvas/formula inspection, network
// self-containment check. Writes artifacts into caps/03-quatro/audit/.
//
// Usage: NODE_PATH=<scratch>/node_modules node caps/03-quatro/audit.mjs
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
  script: 'caps/03-quatro/audit.mjs',
  code_commit: execSync('git rev-parse --short HEAD', { cwd: chapterDir }).toString().trim(),
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

  // -- interaction: probe at x=2 must read the triple value 4,0000
  //    (independent expectation: 2+2, 2*2, pow(2,2) are all exactly 4)
  await page.fill('#probe', '200');
  await page.dispatchEvent('#probe', 'input');
  const at2 = await page.textContent('#leitura');
  check(`${name}.probe_triple_at_x2`,
    at2.includes('x = 2,00') && at2.includes('x+x = 4,0000')
    && at2.includes('x·x = 4,0000') && at2.includes('x^x = 4,0000')
    && at2.includes('as três coincidem'),
    `"${at2.slice(0, 110)}…"`);

  // -- probe at x=1: pairwise (x·x = x^x = 1) but NOT triple (x+x = 2)
  await page.fill('#probe', '100');
  await page.dispatchEvent('#probe', 'input');
  const at1 = await page.textContent('#leitura');
  check(`${name}.probe_pairwise_at_x1`,
    at1.includes('x+x = 2,0000') && at1.includes('x·x = 1,0000')
    && at1.includes('x^x = 1,0000') && at1.includes('duas coincidem')
    && !at1.includes('as três coincidem'));

  // -- nudge buttons move the probe by 0,01
  await page.click('#btn-right');
  const nudged = await page.textContent('#leitura');
  await page.click('#btn-left');
  const back = await page.textContent('#leitura');
  check(`${name}.nudge_buttons`, nudged.includes('x = 1,01') && back.includes('x = 1,00'));

  // -- keyboard operability: slider responds to arrow keys, button to Enter
  await page.focus('#probe');
  await page.keyboard.press('ArrowRight');
  const afterArrow = await page.textContent('#leitura');
  await page.focus('#btn-reset');
  await page.keyboard.press('Enter');
  const afterEnter = await page.textContent('#leitura');
  check(`${name}.keyboard_activation`,
    afterArrow.includes('x = 1,01') && afterEnter.includes('x = 1,00'));

  // -- window slider rescales and announces
  await page.fill('#xmax', '400');
  await page.dispatchEvent('#xmax', 'input');
  const winLabel = await page.textContent('#xmax-val');
  check(`${name}.window_control`, winLabel.trim() === '0 ≤ x ≤ 4,0');

  // -- small window: the hidden root region (x^x above 2x below x=0.35)
  await page.fill('#xmax', '120'); await page.dispatchEvent('#xmax', 'input');
  await page.fill('#probe', '30'); await page.dispatchEvent('#probe', 'input');
  const at03 = await page.textContent('#leitura');
  // independent expectation: 0.3^0.3 = 0.6968... > 2*0.3 = 0.6
  check(`${name}.small_root_region_readable`,
    at03.includes('x = 0,30') && at03.includes('x+x = 0,6000')
    && at03.includes('x^x = 0,6968'), `"${at03.slice(0, 90)}…"`);
  await page.click('#btn-reset');

  // -- overflow / clipping
  const overflow = await page.evaluate(() =>
    document.documentElement.scrollWidth > document.documentElement.clientWidth);
  check(`${name}.no_horizontal_overflow`, !overflow);

  // -- canvas: labeled, sized, actually painted. Read EVERY pixel —
  //    sparse strides alias against thin traces (chapter 1 audit incident).
  const canvasInfo = await page.evaluate(() => {
    return [...document.querySelectorAll('canvas')].map(c => {
      const d = c.getContext('2d').getImageData(0, 0, c.width, c.height).data;
      let painted = 0;
      for (let i = 3; i < d.length; i += 4) if (d[i] !== 0) painted++;
      return { label: c.getAttribute('aria-label') ?? '', w: c.width, h: c.height,
               paintedShare: painted / (d.length / 4) };
    });
  });
  check(`${name}.canvas_labeled_and_painted`,
    canvasInfo.length === 1 && canvasInfo.every(c => c.label.length > 20 && c.paintedShare > 0.001),
    canvasInfo.map(c => c.paintedShare.toFixed(4)).join(', '));

  // -- canvas stays painted across the window range (every pixel read)
  const paintedAt = async (xmaxVal) => {
    await page.fill('#xmax', xmaxVal); await page.dispatchEvent('#xmax', 'input');
    return page.evaluate(() => {
      const c = document.getElementById('cv-plot');
      const d = c.getContext('2d').getImageData(0, 0, c.width, c.height).data;
      let p = 0;
      for (let i = 3; i < d.length; i += 4) if (d[i] !== 0) p++;
      return p / (d.length / 4);
    });
  };
  const p12 = await paintedAt('120');
  const p40 = await paintedAt('400');
  check(`${name}.canvas_painted_across_window_range`,
    p12 > 0.001 && p40 > 0.001, `share xmax=1,2: ${p12.toFixed(4)}, xmax=4,0: ${p40.toFixed(4)}`);
  await page.click('#btn-reset');

  // -- formulas are text (no images), live region present, table static rows
  const dom = await page.evaluate(() => ({
    formulaCount: document.querySelectorAll('.formula').length,
    imgCount: document.querySelectorAll('img').length,
    liveRegion: !!document.querySelector('[aria-live]'),
    tableRows: document.querySelectorAll('tbody tr').length,
    exCount: document.querySelectorAll('.exercicio').length,
    gabCount: document.querySelectorAll('details.gab').length,
  }));
  check(`${name}.formulas_textual_no_images`, dom.formulaCount >= 6 && dom.imgCount === 0,
    `formulas=${dom.formulaCount}, imgs=${dom.imgCount}`);
  check(`${name}.aria_live_region_present`, dom.liveRegion);
  check(`${name}.integer_table_rows`, dom.tableRows === 5, `rows=${dom.tableRows} (k = 1..5)`);

  // -- exercises (E20): >= 10, every one with a details.gab
  check(`${name}.exercises_with_gabaritos`, dom.exCount >= 10 && dom.gabCount >= dom.exCount,
    `exercicios=${dom.exCount}, gabaritos=${dom.gabCount}`);
  await page.click('details.gab summary >> nth=0');
  const gabOpens = await page.evaluate(() => document.querySelector('details.gab').open);
  await page.click('details.gab summary >> nth=0');
  check(`${name}.gabarito_keyboard_toggle`, gabOpens);

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
