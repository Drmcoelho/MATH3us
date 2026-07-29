// Gate v0 audit for Chapter 7 (caps/07-complexos), MATH3us.md §1.7.
// Adapted from caps/02-ternas/audit.mjs for this chapter's controls.
// Screenshots (desktop + iPhone viewport), interaction tests against
// independent in-test computations, keyboard operability, overflow /
// canvas / formula inspection, network self-containment check, and the
// E11 containment check: the notation e^{iθ} (written e<sup>i…</sup> in
// the HTML) must occur ONLY inside door-marked regions.
// Writes artifacts into caps/07-complexos/audit/.
//
// Usage:
//   NODE_PATH=<scratchpad>/node_modules node caps/07-complexos/audit.mjs
import { createRequire } from 'module';
import { existsSync, writeFileSync, readFileSync } from 'fs';
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
  script: 'caps/07-complexos/audit.mjs',
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
const near = (a, b, tol = 1e-3) => Math.abs(a - b) <= tol;
const parseBR = (s) => Number(String(s).replace(/\./g, '').replace(',', '.').replace('−', '-'));

// ---------- E11 containment: raw-source check (browser-independent) ------
{
  const html = readFileSync(resolve(chapterDir, 'index.html'), 'utf8');
  const regions = [];
  const reStart = /<!-- door-exp:start -->/g;
  let m;
  while ((m = reStart.exec(html)) !== null) {
    const end = html.indexOf('<!-- door-exp:end -->', m.index);
    if (end === -1) { regions.length = 0; break; }
    regions.push([m.index, end]);
  }
  const occ = [...html.matchAll(/e<sup>i/g)].map((x) => x.index);
  const outside = occ.filter((i) => !regions.some(([a, b]) => i >= a && i <= b));
  check('eitheta_notation_contained_in_door_boxes',
    regions.length >= 2 && occ.length >= 1 && outside.length === 0,
    `regions=${regions.length}, occurrences=${occ.length}, outside=${outside.length}`);
  // and no unescaped plain-text variants sneak in
  const plain = [...html.matchAll(/e\^\{?i/g)].map((x) => x.index)
    .filter((i) => !regions.some(([a, b]) => i >= a && i <= b));
  check('eitheta_no_plaintext_variant_outside', plain.length === 0,
    plain.length ? `found at ${plain.join(',')}` : 'none');
}

const browser = await chromium.launch({ executablePath: exePath });

async function auditViewport(name, viewport) {
  const page = await browser.newPage({ viewport });
  const external = [];
  page.on('request', (r) => { if (!r.url().startsWith('file://')) external.push(r.url()); });
  page.on('console', (msg) => { if (msg.type() === 'error') report.errors.push(`[${name}] ${msg.text()}`); });
  page.on('pageerror', (e) => report.errors.push(`[${name}] ${e.message}`));
  await page.goto(pageUrl);

  // ===== laboratory A: multiplication ====================================
  // independent expectation: z = 3 + 1i, w = 1 - 2i  ->  zw = 5 - 5i
  await page.fill('#za', '3');
  await page.dispatchEvent('#za', 'input');
  await page.fill('#wb', '-2');
  await page.dispatchEvent('#wb', 'input');
  const multCells = await page.evaluate(() =>
    [...document.querySelectorAll('#tabela-mult-corpo tr')].map((tr) =>
      [...tr.children].map((td) => td.textContent)));
  const zw = multCells[2]; // row "z·w": [name, Re, Im, N, |.|, angle]
  const eRe = 3 * 1 - 1 * (-2), eIm = 3 * (-2) + 1 * 1; // 5, -5
  const eN = eRe * eRe + eIm * eIm;                      // 50
  check(`${name}.mult_product_vs_independent`,
    multCells.length === 4 && zw[0] === 'z·w' &&
    near(parseBR(zw[1]), eRe) && near(parseBR(zw[2]), eIm) &&
    near(parseBR(zw[3]), eN) &&
    near(parseBR(zw[5]), Math.atan2(eIm, eRe) * 180 / Math.PI, 0.02),
    `row=${JSON.stringify(zw)}`);
  const normRow = multCells[3];
  check(`${name}.mult_norm_identity_row`,
    near(parseBR(normRow[2]), (9 + 1) * (1 + 4)) && normRow[3].includes('✓'),
    `N(z)N(w)=${normRow[2]} check=${normRow[3]}`);
  const stM = await page.textContent('#leitura-mult');
  check(`${name}.mult_status_defect_zero_here`,
    stM.includes('defeito de ramo: 0°'), stM.slice(0, 90));
  // reset restores the worked example (2+i)(1+3i) = -1+7i
  await page.click('#btn-mult-reset');
  const stM2 = await page.textContent('#leitura-mult');
  check(`${name}.mult_reset_worked_example`,
    stM2.includes('-1,00 + 7,00i'), stM2.slice(0, 120));
  // degenerate: z = 0 announces undefined argument
  await page.fill('#za', '0'); await page.dispatchEvent('#za', 'input');
  await page.fill('#zb', '0'); await page.dispatchEvent('#zb', 'input');
  const stM0 = await page.textContent('#leitura-mult');
  check(`${name}.mult_degenerate_zero_declared`, stM0.includes('argumento indefinido'));
  await page.click('#btn-mult-reset');

  // ===== laboratory B: n-th roots ========================================
  await page.fill('#w-mod', '2'); await page.dispatchEvent('#w-mod', 'input');
  await page.fill('#w-arg', '60'); await page.dispatchEvent('#w-arg', 'input');
  await page.fill('#n-idx', '5'); await page.dispatchEvent('#n-idx', 'input');
  const rootRows = await page.evaluate(() =>
    [...document.querySelectorAll('#tabela-roots-corpo tr')].map((tr) =>
      [...tr.children].map((td) => td.textContent)));
  // independent: r = 2^(1/5), z0 at (60/5)° = 12°
  const r5 = Math.pow(2, 1 / 5);
  const z0re = r5 * Math.cos(12 * Math.PI / 180), z0im = r5 * Math.sin(12 * Math.PI / 180);
  check(`${name}.roots_count_and_z0_vs_independent`,
    rootRows.length === 5 &&
    near(parseBR(rootRows[0][2]), z0re, 1e-3) &&
    near(parseBR(rootRows[0][3]), z0im, 1e-3) &&
    rootRows.every((row) => parseBR(row[4].replace('e-', 'E-')) < 1e-9),
    `rows=${rootRows.length}, z0=(${rootRows[0]?.[2]}, ${rootRows[0]?.[3]})`);
  const stR = await page.textContent('#leitura-roots');
  check(`${name}.roots_multivalence_counter`,
    stR.includes('5 raízes distintas') && stR.includes('k = 0 de {0, …, 4}'),
    stR.slice(0, 120));
  // keyboard operability: focus the cycle button, activate with Enter
  await page.focus('#btn-next-root');
  await page.keyboard.press('Enter');
  const stR1 = await page.textContent('#leitura-roots');
  check(`${name}.roots_keyboard_next_k1`, stR1.includes('k = 1 de {0, …, 4}'));
  // degenerate w = 0 declared
  await page.fill('#w-mod', '0'); await page.dispatchEvent('#w-mod', 'input');
  const stR0 = await page.textContent('#leitura-roots');
  check(`${name}.roots_degenerate_w0_declared`,
    stR0.includes('degenerado') && stR0.includes('única solução'));
  await page.fill('#w-mod', '2'); await page.dispatchEvent('#w-mod', 'input');

  // ===== laboratory C: the lattice =======================================
  await page.fill('#p-idx', '5'); await page.dispatchEvent('#p-idx', 'input'); // p = 13
  const stL13 = await page.textContent('#leitura-lattice');
  check(`${name}.lattice_p13_decomposition`,
    stL13.includes('13 = 2² + 3²') && stL13.includes('(2 + 3i)(2 − 3i)'),
    stL13.slice(0, 120));
  await page.fill('#p-idx', '7'); await page.dispatchEvent('#p-idx', 'input'); // p = 19
  const stL19 = await page.textContent('#leitura-lattice');
  check(`${name}.lattice_p19_provably_dark`,
    stL19.includes('provadamente escuro') && stL19.includes('19'),
    stL19.slice(0, 120));
  // keyboard: next-prime button via Enter -> 23
  await page.focus('#btn-next-prime');
  await page.keyboard.press('Enter');
  const stL23 = await page.textContent('#leitura-lattice');
  check(`${name}.lattice_keyboard_next_prime`, stL23.includes('23'));
  const latTable = await page.evaluate(() => {
    const rows = [...document.querySelectorAll('#tabela-lattice-corpo tr')];
    const cur = document.querySelector('#tabela-lattice-corpo tr.atual');
    return { count: rows.length, cur: cur ? cur.children[0].textContent : null,
             first: rows[0] ? [...rows[0].children].map((td) => td.textContent) : [] };
  });
  check(`${name}.lattice_table_25_primes_highlight`,
    latTable.count === 25 && latTable.cur === '23' &&
    latTable.first.join('|') === '2|2|1² + 1²|ramifica: −i(1+i)²',
    `rows=${latTable.count}, cur=${latTable.cur}`);

  // ===== overflow / clipping =============================================
  const overflow = await page.evaluate(() =>
    document.documentElement.scrollWidth > document.documentElement.clientWidth);
  check(`${name}.no_horizontal_overflow`, !overflow);

  // ===== canvases: labeled, actually painted (read EVERY pixel) ==========
  const canvasInfo = await page.evaluate(() =>
    [...document.querySelectorAll('canvas')].map((c) => {
      const d = c.getContext('2d').getImageData(0, 0, c.width, c.height).data;
      let painted = 0;
      for (let i = 3; i < d.length; i += 4) if (d[i] !== 0) painted++;
      return { label: c.getAttribute('aria-label') ?? '', w: c.width, h: c.height,
               paintedShare: painted / (d.length / 4) };
    }));
  check(`${name}.canvases_labeled_and_painted`,
    canvasInfo.length === 3 && canvasInfo.every((c) => c.label.length > 20 && c.paintedShare > 0.001),
    canvasInfo.map((c) => c.paintedShare.toFixed(4)).join(', '));

  // repaint across parameter sweeps without going blank
  let alwaysPainted = true;
  for (const [id, vals] of [['za', ['-4', '4']], ['n-idx', ['2', '12']], ['p-idx', ['0', '45']]]) {
    for (const v of vals) {
      await page.fill('#' + id, v);
      await page.dispatchEvent('#' + id, 'input');
      const shares = await page.evaluate(() =>
        [...document.querySelectorAll('canvas')].map((c) => {
          const d = c.getContext('2d').getImageData(0, 0, c.width, c.height).data;
          let p = 0;
          for (let i = 3; i < d.length; i += 4) if (d[i] !== 0) p++;
          return p / (d.length / 4);
        }));
      if (!shares.every((s) => s > 0.001)) alwaysPainted = false;
    }
  }
  check(`${name}.canvases_never_blank_across_range`, alwaysPainted);

  // ===== formulas, live regions, anchors, exercises ======================
  const dom = await page.evaluate(() => ({
    formulaCount: document.querySelectorAll('.formula').length,
    imgCount: document.querySelectorAll('img').length,
    liveRegions: document.querySelectorAll('[aria-live]').length,
    exCount: document.querySelectorAll('.exercicio').length,
    gabCount: document.querySelectorAll('details.gab').length,
    doorBoxes: document.querySelectorAll('[data-door-exp]').length,
    anchors: ['por-que', 'fundacao-geometrica', 'definicoes-trig', 'construcao', 'corpo',
              'norma-identidade', 'forma-polar', 'rotacao', 'rotacao-escala',
              'formulas-adicao', 'produto-polar', 'de-moivre', 'raiz-real',
              'raizes-enesimas', 'falha-destruida', 'soma-raizes', 'argumento-ramo',
              'porta-exponencial', 'log-formal', 'inteiros-gaussianos', 'unidades',
              'divisao-gaussiana', 'euclides-gaussiano', 'wilson', 'residuo-quadratico',
              'dois-quadrados', 'algoritmo-gcd', 'primos-gaussianos', 'porta-reaberta',
              'camadas', 'exercicios', 'horizonte']
      .filter((id) => !document.getElementById(id)),
  }));
  check(`${name}.formulas_textual_no_images`, dom.formulaCount >= 8 && dom.imgCount === 0,
    `formulas=${dom.formulaCount}, imgs=${dom.imgCount}`);
  check(`${name}.aria_live_regions_present`, dom.liveRegions >= 3, `live=${dom.liveRegions}`);
  check(`${name}.claims_proof_anchors_exist`, dom.anchors.length === 0,
    dom.anchors.length ? 'missing: ' + dom.anchors.join(',') : 'all 32 anchors present');
  check(`${name}.exercises_with_gabaritos`, dom.exCount >= 13 && dom.gabCount >= dom.exCount,
    `exercicios=${dom.exCount}, gabaritos=${dom.gabCount}`);
  check(`${name}.door_marked_regions_in_dom`, dom.doorBoxes >= 2, `doorBoxes=${dom.doorBoxes}`);
  await page.click('details.gab summary >> nth=0');
  const gabOpens = await page.evaluate(() => document.querySelector('details.gab').open);
  await page.click('details.gab summary >> nth=0');
  check(`${name}.gabarito_toggle`, gabOpens);

  // ===== self-containment ================================================
  check(`${name}.self_contained_no_network`, external.length === 0,
    external.length ? external.join(' ') : 'only file:// requests');

  // ===== screenshot (full page) ==========================================
  await page.click('#btn-mult-reset');
  await page.fill('#n-idx', '3'); await page.dispatchEvent('#n-idx', 'input');
  await page.fill('#p-idx', '5'); await page.dispatchEvent('#p-idx', 'input');
  await page.screenshot({ path: `${auditDir}/${name}.png`, fullPage: true });
  await page.close();
}

await auditViewport('desktop', { width: 1440, height: 900 });
await auditViewport('iphone', { width: 390, height: 844 });
await browser.close();

check('no_console_or_page_errors', report.errors.length === 0,
  report.errors.join(' | ') || undefined);

report.all_passed = Object.values(report.checks).every((c) => c.passed);
writeFileSync(`${auditDir}/interaction-report.json`, JSON.stringify(report, null, 2) + '\n');
console.log(`\n${report.all_passed ? 'AUDIT PASSED' : 'AUDIT FAILED'} — artifacts in ${auditDir}/`);
process.exit(report.all_passed ? 0 : 1);
