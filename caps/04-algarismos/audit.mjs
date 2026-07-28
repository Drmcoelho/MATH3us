// Gate v0 audit for Chapter 4 (Os Algarismos Repetidos) — MATH3us.md §1.7.
// Adapted from tools/audit.mjs to this page's controls (a/d inputs, base
// select, presets, digit stream, state-machine table). Screenshots in
// desktop and iPhone viewports; interaction correctness verified against
// an IN-TEST independent long-division implementation; keyboard
// operability; overflow; formulas; aria-live; self-containment; exercises.
//
// Usage: NODE_PATH=<scratch>/node_modules node caps/04-algarismos/audit.mjs
import { createRequire } from 'module';
import { existsSync, writeFileSync } from 'fs';
import { resolve, dirname } from 'path';
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
  script: 'caps/04-algarismos/audit.mjs',
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

// In-test INDEPENDENT long-division implementation (observation cross-check).
function machineRef(a, d, b) {
  const q = Math.floor(a / d);
  let r = a % d;
  const seen = new Map(), digits = [];
  while (r !== 0 && !seen.has(r)) {
    seen.set(r, digits.length);
    const t = b * r;
    digits.push(Math.floor(t / d));
    r = t % d;
  }
  if (r === 0) return { q, pre: digits, per: [] };
  const i = seen.get(r);
  return { q, pre: digits.slice(0, i), per: digits.slice(i) };
}
const CH = '0123456789ABCDEF';
const joinRef = (arr, b) => arr.map(v => b <= 16 ? CH[v] : String(v)).join(b === 60 ? ':' : '');

const browser = await chromium.launch({ executablePath: exePath });

async function setAndRun(page, a, d, b) {
  await page.fill('#inp-a', String(a));
  await page.fill('#inp-d', String(d));
  await page.selectOption('#sel-b', String(b));
  await page.click('#btn-run');
}

async function auditViewport(name, viewport) {
  const page = await browser.newPage({ viewport });
  const external = [];
  page.on('request', r => { if (!r.url().startsWith('file://')) external.push(r.url()); });
  page.on('console', m => { if (m.type() === 'error') report.errors.push(`[${name}] ${m.text()}`); });
  page.on('pageerror', e => report.errors.push(`[${name}] ${e.message}`));
  await page.goto(pageUrl);

  // -- initial state: 1/7 base 10, verified against the reference impl
  const ref7 = machineRef(1, 7, 10);
  const status0 = await page.textContent('#leitura');
  const verd0 = await page.textContent('#veredito');
  check(`${name}.initial_1_7_base10_status`,
    status0.includes('expansão de 1/7 na base 10') &&
    status0.includes(`pré-período ${ref7.pre.length}`) &&
    status0.includes(`período ${ref7.per.length}`),
    `"${status0.slice(0, 90)}…" vs ref pre=${ref7.pre.length} per=${ref7.per.length}`);
  check(`${name}.initial_1_7_digits_match_reference`,
    verd0.includes('período = ' + joinRef(ref7.per, 10)),
    `expected block ${joinRef(ref7.per, 10)}`);

  // -- pre-period case 5/12 base 10 against reference
  const ref512 = machineRef(5, 12, 10);
  await setAndRun(page, 5, 12, 10);
  const s512 = await page.textContent('#leitura');
  const v512 = await page.textContent('#veredito');
  check(`${name}.interaction_5_12_base10`,
    s512.includes('expansão de 5/12 na base 10') &&
    s512.includes(`pré-período ${ref512.pre.length}`) &&
    s512.includes(`período ${ref512.per.length}`) &&
    v512.includes('pré-período = ' + joinRef(ref512.pre, 10)) &&
    v512.includes('período = ' + joinRef(ref512.per, 10)),
    `ref pre=${joinRef(ref512.pre, 10)} per=${joinRef(ref512.per, 10)}`);

  // -- automatic reduction displayed (Enunciado C in the lab)
  await page.click('.presets button:has-text("2/6 na base 10")');
  const red = await page.textContent('#reducao');
  const sred = await page.textContent('#leitura');
  check(`${name}.unreduced_2_6_reduced_and_recorded`,
    red.includes('reduzida automaticamente para 1/3') && sred.includes('expansão de 1/3 na base 10'),
    `"${red.slice(0, 80)}"`);

  // -- base 60 rendering (colon-separated) against reference
  const ref760 = machineRef(1, 7, 60);
  await setAndRun(page, 1, 7, 60);
  const v760 = await page.textContent('#veredito');
  check(`${name}.base60_colon_digits`,
    v760.includes('período = ' + joinRef(ref760.per, 60)),
    `expected ${joinRef(ref760.per, 60)}`);

  // -- exact expansion in matching base (1/7 base 7)
  await setAndRun(page, 1, 7, 7);
  const s77 = await page.textContent('#leitura');
  check(`${name}.termination_detector_1_7_base7`,
    s77.includes('pré-período 1, período 0'),
    `"${s77.slice(0, 90)}"`);
  const v77 = await page.textContent('#veredito');
  check(`${name}.criterion_verdict_shown`, v77.includes('termina'), undefined);

  // -- adversarial input refused politely
  await page.fill('#inp-d', '0');
  await page.click('#btn-run');
  const sBad = await page.textContent('#leitura');
  check(`${name}.d_zero_refused`, sBad.includes('Entrada recusada'), `"${sBad.slice(0, 70)}"`);

  // -- long period case (large prime): stream must wrap, page must not scroll horizontally
  await setAndRun(page, 1, 9973, 10);
  const s9973 = await page.textContent('#leitura');
  check(`${name}.large_prime_9973_period_554`, s9973.includes('período 554'),
    `"${s9973.slice(0, 90)}"`);
  const overflow = await page.evaluate(() =>
    document.documentElement.scrollWidth > document.documentElement.clientWidth);
  check(`${name}.no_horizontal_overflow_with_long_stream`, !overflow);

  // -- keyboard operability: type into d, Enter runs; preset reachable by keyboard
  await page.fill('#inp-d', '13');
  await page.fill('#inp-a', '1');
  await page.selectOption('#sel-b', '10');
  await page.focus('#inp-d');
  await page.keyboard.press('Enter');
  const s13 = await page.textContent('#leitura');
  const ref13 = machineRef(1, 13, 10);
  check(`${name}.keyboard_enter_runs`,
    s13.includes('expansão de 1/13 na base 10') && s13.includes(`período ${ref13.per.length}`),
    `"${s13.slice(0, 80)}"`);
  await page.focus('.presets button:has-text("1/7 na base 10")');
  await page.keyboard.press('Enter');
  const sPreset = await page.textContent('#leitura');
  check(`${name}.keyboard_preset_activation`, sPreset.includes('expansão de 1/7 na base 10'));

  // -- state-machine table mirrors the run (6 data rows for 1/7 + observação column)
  const rows = await page.evaluate(() => {
    const trs = [...document.querySelectorAll('#tabela-corpo tr')];
    return { n: trs.length, last: trs.length ? trs[trs.length - 1].textContent : '' };
  });
  check(`${name}.state_machine_table_mirrors_run`,
    rows.n === 6 && rows.last.includes('ciclo fecha'),
    `rows=${rows.n}, last="${rows.last.slice(0, 60)}"`);

  // -- DOM inventory: formulas textual, no images, aria-live, no canvas
  const dom = await page.evaluate(() => ({
    formulaCount: document.querySelectorAll('.formula').length,
    imgCount: document.querySelectorAll('img').length,
    liveRegion: !!document.querySelector('[aria-live]'),
    canvasCount: document.querySelectorAll('canvas').length,
    exCount: document.querySelectorAll('.exercicio').length,
    gabCount: document.querySelectorAll('details.gab').length,
    streamHasMarkers: !!document.querySelector('#stream .per-d'),
  }));
  check(`${name}.formulas_textual_no_images`, dom.formulaCount >= 6 && dom.imgCount === 0,
    `formulas=${dom.formulaCount}, imgs=${dom.imgCount}`);
  check(`${name}.aria_live_region_present`, dom.liveRegion);
  check(`${name}.no_canvas_by_design_tables_instead`, dom.canvasCount === 0,
    `canvases=${dom.canvasCount} (chapter uses digit streams + tables; no canvas to audit)`);
  check(`${name}.stream_period_markers_present`, dom.streamHasMarkers);

  // -- exercises (E20): tiers present, each with details/summary gabarito
  check(`${name}.exercises_with_gabaritos`, dom.exCount >= 13 && dom.gabCount >= dom.exCount,
    `exercicios=${dom.exCount}, gabaritos=${dom.gabCount}`);
  await page.click('details.gab summary >> nth=0');
  const gabOpens = await page.evaluate(() => document.querySelector('details.gab').open);
  await page.click('details.gab summary >> nth=0');
  check(`${name}.gabarito_toggle`, gabOpens);

  // -- self-containment: zero non-file requests
  check(`${name}.self_contained_no_network`, external.length === 0,
    external.length ? external.join(' ') : 'only file:// requests');

  // -- screenshot (full page) at a representative state
  await page.click('.presets button:has-text("5/12 na base 10")');
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
