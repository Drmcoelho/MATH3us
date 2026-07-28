// Gate v1 claims validator (MATH3us.md §1.7, duties fixed by E13).
// Usage: node tools/verify-claims.mjs caps/01-exaustao
// Dependencies: js-yaml (required), ajv (optional — schema layer skipped
// with a warning if absent). Resolve via node_modules or NODE_PATH.
//
// E13 duties implemented:
//   1. schema validity (schemas/claims.schema.json)
//   2. unique ids inside the chapter namespace chapter-NN.*
//   3. dependencies existing and resolvable — a typo cannot create a
//      silent phantom dependency; cross-chapter targets must belong to
//      a closed chapter (release manifest present) or be marked door: true
//   4. no dependency cycles
//   5. proof anchors existing in the chapter's index.html
//   6. audit artifacts existing at the declared paths
//   7. kind/status/proof_mode compatibility
import { createRequire } from 'module';
import { readFileSync, existsSync, readdirSync } from 'fs';
import { resolve, join, dirname } from 'path';
import { fileURLToPath } from 'url';

const require = createRequire(import.meta.url);
const yaml = require('js-yaml');

const chapterDir = resolve(process.argv[2] ?? '.');
const repoRoot = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const errors = [];
const warnings = [];
const fail = (m) => errors.push(m);

const doc = yaml.load(readFileSync(join(chapterDir, 'claims.yml'), 'utf8'));
const claims = doc.claims ?? [];
const nn = String(doc.chapter).padStart(2, '0');

// ---- 1. schema --------------------------------------------------------
try {
  const Ajv = require('ajv');
  const schema = JSON.parse(
    readFileSync(join(repoRoot, 'schemas', 'claims.schema.json'), 'utf8'));
  const validate = new Ajv({ allErrors: true }).compile(schema);
  if (!validate(doc)) {
    for (const e of validate.errors) fail(`schema: ${e.instancePath || '/'} ${e.message}`);
  }
} catch (e) {
  if (e.code === 'MODULE_NOT_FOUND') warnings.push('ajv unavailable — schema layer skipped');
  else throw e;
}

// ---- 2. unique ids, correct namespace ---------------------------------
const ids = new Set();
for (const c of claims) {
  if (!c.id) { fail('claim missing id'); continue; }
  if (ids.has(c.id)) fail(`duplicate id: ${c.id}`);
  ids.add(c.id);
  if (!c.id.startsWith(`chapter-${nn}.`)) fail(`${c.id}: outside namespace chapter-${nn}.*`);
}

// ---- 3. dependencies resolvable ---------------------------------------
const manifestsDir = join(repoRoot, 'releases', 'manifests');
const closedChapters = new Set(
  (existsSync(manifestsDir) ? readdirSync(manifestsDir) : [])
    .map((f) => (f.match(/^cap-(\d{2})-/) || [])[1]).filter(Boolean));
const foreignLedgers = new Map(); // chapter NN -> Set(ids)
function foreignIds(chNN) {
  if (foreignLedgers.has(chNN)) return foreignLedgers.get(chNN);
  let found = new Set();
  const capsDir = join(repoRoot, 'caps');
  for (const d of existsSync(capsDir) ? readdirSync(capsDir) : []) {
    if (!d.startsWith(chNN + '-')) continue;
    const p = join(capsDir, d, 'claims.yml');
    if (existsSync(p)) {
      const other = yaml.load(readFileSync(p, 'utf8'));
      found = new Set((other.claims ?? []).map((c) => c.id));
    }
  }
  foreignLedgers.set(chNN, found);
  return found;
}
for (const c of claims) {
  for (const d of c.dependencies ?? []) {
    const target = d.claim;
    if (!target) { fail(`${c.id}: dependency without claim id`); continue; }
    if (ids.has(target)) continue; // internal
    const chNN = (target.match(/^chapter-(\d{2})\./) || [])[1];
    if (!chNN) { fail(`${c.id}: malformed dependency "${target}"`); continue; }
    if (!foreignIds(chNN).has(target)) {
      fail(`${c.id}: unresolvable dependency "${target}" (phantom — typo?)`);
      continue;
    }
    if (!closedChapters.has(chNN) && d.door !== true) {
      fail(`${c.id}: depends on open chapter ${chNN} without door: true`);
    }
  }
}

// ---- 4. no cycles (internal graph) ------------------------------------
const adj = new Map(claims.map((c) => [c.id,
  (c.dependencies ?? []).map((d) => d.claim).filter((t) => ids.has(t))]));
const state = new Map();
function dfs(u, stack) {
  state.set(u, 1); stack.push(u);
  for (const v of adj.get(u) ?? []) {
    if (state.get(v) === 1) fail(`dependency cycle: ${[...stack, v].join(' -> ')}`);
    else if (!state.get(v)) dfs(v, stack);
  }
  state.set(u, 2); stack.pop();
}
for (const c of claims) if (!state.get(c.id)) dfs(c.id, []);

// ---- 5. proof anchors exist in index.html -----------------------------
const html = readFileSync(join(chapterDir, 'index.html'), 'utf8');
const anchors = new Set([...html.matchAll(/id="([^"]+)"/g)].map((m) => m[1]));
for (const c of claims) {
  if (c.proof_location?.startsWith('#') && !anchors.has(c.proof_location.slice(1))) {
    fail(`${c.id}: proof_location ${c.proof_location} has no matching id in index.html`);
  }
  if (c.proof_mode === 'proved_here' && !c.proof_location) {
    fail(`${c.id}: proved_here without proof_location`);
  }
}

// ---- 6. artifacts exist -----------------------------------------------
for (const c of claims) {
  for (const [leg, v] of Object.entries(c.verification ?? {})) {
    if (v.status === 'passed') {
      if (!v.artifact) fail(`${c.id}: ${leg} passed without artifact (E12)`);
      else if (!existsSync(join(chapterDir, v.artifact))) {
        fail(`${c.id}: ${leg} artifact missing on disk: ${v.artifact}`);
      }
    }
  }
}
for (const runName of ['oracle_run', 'audit_run']) {
  const run = doc[runName];
  if (!run) continue;
  for (const key of ['report', 'edge_report', 'interaction_report']) {
    if (run[key] && !existsSync(join(repoRoot, run[key]))) {
      fail(`${runName}.${key} missing on disk: ${run[key]}`);
    }
  }
  for (const s of run.screenshots ?? []) {
    if (!existsSync(join(repoRoot, s))) fail(`${runName} screenshot missing: ${s}`);
  }
}

// ---- 7. kind/status/proof_mode compatibility --------------------------
for (const c of claims) {
  const { id, kind, status, proof_mode: pm } = c;
  if (kind === 'synthesis' && pm === 'proved_here') {
    fail(`${id}: synthesis cannot be proved_here — the provable identity is a theorem (E6)`);
  }
  if (kind === 'conjecture' && status === 'proved') {
    fail(`${id}: a proved conjecture must be promoted to theorem/lemma`);
  }
  if (kind === 'question' && !['open', 'conditional'].includes(status)) {
    fail(`${id}: question must have status open or conditional`);
  }
  if (status === 'proved' && !['theorem', 'lemma', 'definition'].includes(kind)) {
    fail(`${id}: status proved requires kind theorem/lemma/definition`);
  }
  if (status === 'proved' && !['proved_here', 'cited'].includes(pm)) {
    fail(`${id}: status proved requires proof_mode proved_here or cited`);
  }
  if (status === 'refuted' && !(c.autopsy || c.correction_log || c.notes)) {
    fail(`${id}: refuted without autopsy/correction_log/notes (§1.3)`);
  }
}

// ---- report -----------------------------------------------------------
for (const w of warnings) console.log(`warn ${w}`);
if (errors.length) {
  for (const e of errors) console.log(`FAIL ${e}`);
  console.log(`\n${errors.length} error(s) — release BLOCKED (gate v1).`);
  process.exit(1);
}
console.log(`ok   ${claims.length} claims valid — schema, ids, dependencies, cycles, anchors, artifacts, compatibility.`);
