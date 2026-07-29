// Gate v0 audit for Chapter 6 (caps/06-patologias), MATH3us.md §1.7.
// Adapted from tools/audit.mjs and the wave-1 chapter audits for this
// chapter's control IDs (the lying plotter + the dyadic probe).
// Screenshots (desktop + iPhone viewport), interaction tests against
// in-test independent computations, keyboard operability, overflow /
// canvas / formula inspection, network self-containment check.
// Writes artifacts into caps/06-patologias/audit/.
//
// Usage:
//   NODE_PATH=<scratchpad>/node_modules node caps/06-patologias/audit.mjs
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
  script: 'caps/06-patologias/audit.mjs',
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

// ---- in-test independent computations (NOT read from the page) ----------
function totientSumIndependent(Q) {           // for the Farey table
  const phi = Array.from({ length: Q + 1 }, (_, i) => i);
  for (let p = 2; p <= Q; p++) {
    if (phi[p] === p) for (let m = p; m <= Q; m += p) phi[m] -= Math.floor(phi[m] / p);
  }
  let s = 0; for (let q = 1; q <= Q; q++) s += phi[q];
  return s;
}
function probeS(pNum, pDen, m) {              // digit-formula S_m over BigInt
  const j = ((1n << BigInt(m)) * pNum) / pDen;
  let S = 0;
  for (let b = 0; b < m; b++) S += ((j >> BigInt(b)) & 1n) === 0n ? 1 : -1;
  return { j, S };
}
const FLOAT_P = 6369051672525773n, FLOAT_Q = 9007199254740992n; // float(sqrt2/2)
function sawJs(x) { return Math.abs(x - Math.round(x)); }
function takagiPartialJs(x, N) {
  let t = 0, p = 1;
  for (let k = 0; k < N; k++) { t += sawJs(x * p) / p; p *= 2; }
  return t;
}
function fmtBR(n) { return Number(n).toLocaleString('pt-BR'); }

const CLAIM_ANCHORS = [
  'por-que', 'experimento', 'sonda', 'padroes', 'enunciados', 'continuidade-def',
  'provas', 'cunha-sqrt2', 'arquimediana', 'densidade-q', 'densidade-irr',
  'dirichlet-prova', 'thomae-prova', 'takagi-continua', 'takagi-declives',
  'lema-aperto', 'takagi-nao-diferenciavel', 'tvi-prova', 'preservacao-sinal',
  'buraco-q', 'arquitetura', 'camadas', 'floats-racionais', 'exercicios', 'horizonte',
];

const browser = await chromium.launch({ executablePath: exePath });

async function paintedShares(page) {
  return page.evaluate(() =>
    [...document.querySelectorAll('canvas')].map(c => {
      const d = c.getContext('2d').getImageData(0, 0, c.width, c.height).data;
      let p = 0;
      for (let i = 3; i < d.length; i += 4) if (d[i] !== 0) p++;  // EVERY pixel
      return p / (d.length / 4);
    }));
}

async function auditViewport(name, viewport) {
  const page = await browser.newPage({ viewport });
  const external = [];
  page.on('request', r => { if (!r.url().startsWith('file://')) external.push(r.url()); });
  page.on('console', m => { if (m.type() === 'error') report.errors.push(`[${name}] ${m.text()}`); });
  page.on('pageerror', e => report.errors.push(`[${name}] ${e.message}`));
  await page.goto(pageUrl);

  // -- initial state: Dirichlet sampled — one line, all-rational status
  const st0 = await page.textContent('#leitura');
  check(`${name}.dirichlet_sampled_status`,
    st0.includes('dirichlet') && st0.includes('640 amostras') && st0.includes('0 irracionais'),
    `"${st0.slice(0, 90)}…"`);

  // -- ideal mode discloses itself
  await page.click('#btn-ideal');
  const stIdeal = await page.textContent('#leitura');
  check(`${name}.dirichlet_ideal_status`,
    stIdeal.includes('duas retas ideais') && stIdeal.includes('nenhuma amostragem'));

  // -- Farey table against the independent sieve
  const farey = await page.evaluate(() =>
    [...document.querySelectorAll('#tabela-farey-corpo tr')].map(tr =>
      [...tr.children].map(td => td.textContent)));
  const fareyOk = farey.length === 3 &&
    farey[0][1] === fmtBR(totientSumIndependent(10)) &&
    farey[1][1] === fmtBR(totientSumIndependent(100)) &&
    farey[2][1] === fmtBR(totientSumIndependent(1000));
  check(`${name}.farey_counts_vs_independent_sieve`, fareyOk,
    `page: ${farey.map(r => r[1]).join(', ')} vs sieve: 32, 3.044, 304.192`);

  // -- Thomae: continuity points invisible, count matches independent enum
  await page.click('#btn-thomae');
  const stTh = await page.textContent('#leitura');
  // independent enumeration for z = 0 (must mirror the page's declared rule)
  const C = Math.sqrt(2) / 2, w0 = 1;
  const Qcap = Math.max(100, Math.min(4000, Math.floor(Math.sqrt(12000 / w0))));
  let count = 0;
  const g = (a, b) => { while (b) { const t = a % b; a = b; b = t; } return a; };
  for (let q = 1; q <= Qcap; q++) {
    const pLo = Math.ceil(q * (C - 0.5)), pHi = Math.floor(q * (C + 0.5));
    for (let p = pLo; p <= pHi; p++) if (g(Math.abs(p), q) === 1) count++;
  }
  check(`${name}.thomae_status_and_count`,
    stTh.includes('pontos de continuidade visíveis: 0') && stTh.includes(fmtBR(count)),
    `expected ${fmtBR(count)} drawn points in "${stTh.slice(0, 110)}…"`);

  // -- Takagi: status min/max vs independent float evaluation
  await page.click('#btn-takagi');
  await page.fill('#termos', '8');
  await page.dispatchEvent('#termos', 'input');
  const stTk = await page.textContent('#leitura');
  let lo = Infinity, hi = -Infinity;
  for (let i = 0; i <= 640; i++) {
    const x = (C - 0.5) + i / 640;
    const y = takagiPartialJs(x, 8);
    if (y < lo) lo = y; if (y > hi) hi = y;
  }
  const nums = (stTk.match(/[0-9]+,[0-9]{8}/g) || []).map(s => Number(s.replace(',', '.')));
  const tkOk = stTk.includes('T_8') && nums.length >= 2 &&
    Math.abs(nums[0] - lo) < 1e-7 && Math.abs(nums[1] - hi) < 1e-7;
  check(`${name}.takagi_minmax_vs_independent`, tkOk,
    `page nums ${nums.slice(0, 2).join(' ')} vs test ${lo.toFixed(8)} ${hi.toFixed(8)}`);

  // -- deep zoom: partial sum honestly declares its straight segment
  await page.fill('#zoom', '20');
  await page.dispatchEvent('#zoom', 'input');
  const stZoom = await page.textContent('#leitura');
  check(`${name}.takagi_deep_zoom_declares_segment`,
    stZoom.includes('EXATAMENTE um segmento de reta'),
    `z=20, N=8: "${stZoom.slice(-120)}"`);
  await page.fill('#zoom', '0');
  await page.dispatchEvent('#zoom', 'input');

  // -- probe: x = 0 gives S_m = m (m = 12 default)
  const stP0 = await page.textContent('#leitura-sonda');
  const e0 = probeS(0n, 1n, 12);
  check(`${name}.probe_x0_S_equals_m`,
    stP0.includes('S_m = ' + e0.S) && e0.S === 12 && stP0.includes('x = 0'));

  // -- probe: x = 1/3 alternates; check m = 12 and m = 11 vs independent
  await page.click('#btn-x13');
  const stP13a = await page.textContent('#leitura-sonda');
  const e13a = probeS(1n, 3n, 12);
  await page.fill('#m-slider', '11');
  await page.dispatchEvent('#m-slider', 'input');
  const stP13b = await page.textContent('#leitura-sonda');
  const e13b = probeS(1n, 3n, 11);
  check(`${name}.probe_x13_vs_independent`,
    stP13a.includes('S_m = ' + e13a.S) && stP13a.includes('j = ' + e13a.j.toString()) &&
    stP13b.includes('S_m = ' + e13b.S) && e13a.S === 0 && e13b.S === 1,
    `m=12: S=${e13a.S} j=${e13a.j}; m=11: S=${e13b.S}`);

  // -- probe: float preset at full depth vs independent BigInt computation
  await page.click('#btn-xf');
  await page.fill('#m-slider', '52');
  await page.dispatchEvent('#m-slider', 'input');
  const stPf = await page.textContent('#leitura-sonda');
  const ef = probeS(FLOAT_P, FLOAT_Q, 52);
  check(`${name}.probe_float_m52_vs_independent`,
    stPf.includes('S_m = ' + ef.S) && stPf.includes('C5 refutada'),
    `expected S_52 = ${ef.S} (oracle: -8) in "${stPf.slice(0, 110)}…"`);

  // -- probe table mirrors state (highlighted current row)
  const probeTable = await page.evaluate(() => {
    const rows = [...document.querySelectorAll('#tabela-sonda-corpo tr')];
    return { count: rows.length, last: [...rows[rows.length - 1].children].map(td => td.textContent) };
  });
  check(`${name}.probe_table_mirrors_state`,
    probeTable.count === 13 && probeTable.last[0] === '52' && Number(probeTable.last[2]) === ef.S,
    `rows=${probeTable.count}, last=[${probeTable.last.join(', ')}]`);

  // -- keyboard operability: focus button, activate with Enter
  await page.focus('#btn-x0');
  await page.keyboard.press('Enter');
  const afterEnter = await page.textContent('#leitura-sonda');
  check(`${name}.keyboard_activation`,
    afterEnter.includes('x = 0') && afterEnter.includes('S_m = 52'),
    'Enter on #btn-x0 with m = 52');

  // -- overflow / clipping
  const overflow = await page.evaluate(() =>
    document.documentElement.scrollWidth > document.documentElement.clientWidth);
  check(`${name}.no_horizontal_overflow`, !overflow);

  // -- canvases: labeled, painted (EVERY pixel read — aliasing lesson)
  const canvasInfo = await page.evaluate(() =>
    [...document.querySelectorAll('canvas')].map(c => ({
      label: c.getAttribute('aria-label') ?? '', w: c.width, h: c.height })));
  const shares0 = await paintedShares(page);
  check(`${name}.canvases_labeled_and_painted`,
    canvasInfo.length === 3 && canvasInfo.every(c => c.label.length > 20) &&
    shares0.every(s => s > 0.001),
    shares0.map(s => s.toFixed(4)).join(', '));

  // -- canvases never blank across function switches and zoom range
  let alwaysPainted = true;
  for (const fnBtn of ['#btn-dirichlet', '#btn-thomae', '#btn-takagi']) {
    await page.click(fnBtn);
    for (const z of ['0', '10', '20']) {
      await page.fill('#zoom', z);
      await page.dispatchEvent('#zoom', 'input');
      const shares = await paintedShares(page);
      if (!shares.every(s => s > 0.001)) alwaysPainted = false;
    }
  }
  await page.fill('#zoom', '0');
  await page.dispatchEvent('#zoom', 'input');
  check(`${name}.canvases_never_blank_across_range`, alwaysPainted);

  // -- formulas are text (no images), live regions present, anchors exist
  const dom = await page.evaluate((anchors) => ({
    formulaCount: document.querySelectorAll('.formula').length,
    imgCount: document.querySelectorAll('img').length,
    liveRegions: document.querySelectorAll('[aria-live]').length,
    exCount: document.querySelectorAll('.exercicio').length,
    gabCount: document.querySelectorAll('details.gab').length,
    missing: anchors.filter(id => !document.getElementById(id)),
  }), CLAIM_ANCHORS);
  check(`${name}.formulas_textual_no_images`, dom.formulaCount >= 8 && dom.imgCount === 0,
    `formulas=${dom.formulaCount}, imgs=${dom.imgCount}`);
  check(`${name}.aria_live_regions_present`, dom.liveRegions >= 2,
    `${dom.liveRegions} live regions`);
  check(`${name}.claims_proof_anchors_exist`, dom.missing.length === 0,
    dom.missing.length ? 'missing: ' + dom.missing.join(',') : `all ${CLAIM_ANCHORS.length} anchors present`);

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
  await page.click('#btn-dirichlet');
  await page.click('#btn-amostrado');
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
