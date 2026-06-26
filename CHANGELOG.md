# CHANGELOG — `rasa.domain.soccer.goalkeeping`

Reverse-chronological. Each entry is a version bump.

---

## 0.1.0 — 2026-06-25 — INITIAL (Phase 1 shell)

### Forked from rasa.domain.core

Scaffolded via `bin/new-element domain soccer-goalkeeping`, then the
canonical name was hand-set to the dotted form. Inherits canon-required
files (§4) + Apache-2.0 LICENSE + bin/init + bin/check-manifest + seed
templates + content/SHAPE.md (which forks delete after picking a shape
pattern).

### First sub-namespaced domain (canon precedent)

Canonical name **`rasa.domain.soccer.goalkeeping`** — the first domain
to use a dotted `soccer.<specialty>` sub-namespace. Valid because the
schema `ElementName` first-party identifier is `.+`. The folder + repo
use the dashed form `domain-soccer-goalkeeping`; `rasa.json#name` is the
authoritative dotted name (tools read it directly). Alias
`rasa.domain.soccer-goalkeeping` kept for flat-form discoverability.
Decision + rationale recorded in `rasa.json#rasa.naming`.

### State

- `description` filled; `kind: domain`, `contract_version: 1.3.0`,
  `version: 0.1.0`.
- `capabilities[]` empty, `shape_pattern: agnostic`, `content/` is the
  inherited domain-core scaffold — **no goalkeeping content yet.**
- `bin/check-manifest` GREEN; conforms to `RasaOS/schema` v0.1.0.

### TODO before content ship (v0.2.0+)

- Decide shape pattern (`rasa.json#rasa.shape_pattern`): a goalkeeping
  domain is likely a **toolkit** (drills, technique rules, match-prep
  skills) or **hybrid**.
- Populate `content/` (technique/shot-stopping/distribution/positioning
  rules; training-drill templates; match-prep + keeper-development
  skills). Delete `content/SHAPE.md`; add `content/README.md`.
- Fill `capabilities[]` (e.g. `goalkeeping.technique`,
  `goalkeeping.training`, `goalkeeping.match-prep`,
  `goalkeeping.development`).
- Author this Element's own `CLAUDE.md` (currently the generic template).
- Register in `elements/REGISTRY.md` + `elements/CHANGELOG.md`.
