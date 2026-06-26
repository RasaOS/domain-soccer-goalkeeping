# CHANGELOG — `rasa.domain.soccer.goalkeeping`

Reverse-chronological. Each entry is a version bump.

---

## 0.2.0 — 2026-06-25 — Domain core authored from three curricula

The foundational goalkeeping knowledge core — the "foundational
informational for everything going forward." `shape_pattern` moves from
`agnostic` → **`structural`**.

### Sources (preserved verbatim)

Synthesized from three real goalkeeping curricula, kept as the source of
record under `content/reference/sources/` (registered `opt-in` — they ship
with the Element but are not auto-installed):

- **"The GK Trainer"** — *Developing a Training Program for Coaching
  Goalkeeping*, Rob Walker (US National Goalkeeping Staff Coach). The deep
  technical curriculum + the two training methods + U12–U19 load bands.
- **ECNL Goalkeeping Curriculum & Handbook** (Birmingham United Soccer
  Association / BUSA). Philosophy, the four-stage communication syllabus,
  tactical situations, mentality.
- **Goalkeeper Plan 2015–2016**. Organization, the U9–U18 age syllabus,
  the named-drill library, testing.

Lineage recorded in `rasa.json#rasa.sources`; the mapping of each source
into the core is in `content/reference/README.md`.

### What was authored (~39k words across 20 files)

- **`content/PHILOSOPHY.md`** — the manifesto (contrarian identity,
  build-from-essentials, hold-and-react, decision-making, long-term arc).
- **`content/framework/`** — `development-framework` (U9–U12 / U13–U15 /
  U16–U18+ with testing), `training-methodology` (Simple-to-Complex,
  Whole-Part-Whole, session structure, organization, charting),
  `communication-syllabus` (the four-stage command ladder).
- **`content/syllabus/`** — nine technical categories: handling-catching,
  footwork-movement, shot-stopping-diving, aerial-crosses,
  one-v-one-breakaway, distribution, positioning-angles, playing-with-feet,
  psychology-mentality. Each: progressions, coaching cues, faults, stage
  emphasis, related drills, key terms.
- **`content/drills/library.md`** — every named drill as a card
  (objective / setup / execution / cues / syllabus-area), grouped by area.
- **`content/vocabulary.md`** — the merged, deduped glossary (technique +
  the four-stage commands + methodology terms).
- Index READMEs for the core, framework, syllabus, drills, and reference.

Authored faithfully to the sources — no technique or drill invented;
single-source / divergent points flagged in-text (e.g. the cross-source
"power step" naming collision).

### Install shape

The core installs to **`.claude/goalkeeping/`** (`framework/`, `syllabus/`,
`drills/` directory-mirror; `PHILOSOPHY.md` + `vocabulary.md` file-replace;
Element-owned, refreshed on upgrade). `content/README.md` + `content/reference/`
(the PDFs + provenance) ship `opt-in`. Deleted the fork's `content/SHAPE.md`
(replaced by `content/README.md`).

### Verification

`bin/check-manifest` GREEN (33 tracked files, all registered); `schema/bin/validate`
OK; all 20 markdown cross-references resolve; `bin/init` smoke-tested →
core lands in `.claude/goalkeeping/`, PDFs correctly NOT auto-installed.

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
