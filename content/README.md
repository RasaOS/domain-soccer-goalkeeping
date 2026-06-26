---
title: Soccer · Goalkeeping — Domain Core
element: rasa.domain.soccer.goalkeeping
layer: core
---

# Soccer · Goalkeeping — Domain Core

This is the **core** of `rasa.domain.soccer.goalkeeping`: the foundational
goalkeeping knowledge that everything in this domain builds on. It is a
**structural / reference** foundation — synthesized from three real
goalkeeping curricula (see [`reference/`](reference/README.md)) into one
coherent body of coaching knowledge.

> Catching, footwork, positioning — competence in the short term,
> world-class over the long term. Build from the essentials. (See
> [PHILOSOPHY](PHILOSOPHY.md).)

## How the core is organized

| Layer | Path | What it holds |
|---|---|---|
| **Philosophy** | [`PHILOSOPHY.md`](PHILOSOPHY.md) | The coaching manifesto — the *why* behind everything below. |
| **Framework** | [`framework/`](framework/README.md) | The developmental spine: age/level model, training methodology, communication syllabus. |
| **Syllabus** | [`syllabus/`](syllabus/README.md) | The technical/tactical curriculum — nine categories, each with progressions, coaching cues, faults, and stage emphasis. |
| **Drills** | [`drills/library.md`](drills/library.md) | The practical drill library — named exercises as cards, cross-linked to syllabus areas. |
| **Vocabulary** | [`vocabulary.md`](vocabulary.md) | The glossary — technique terms, the four-stage communication commands, methodology terms. |
| **Reference** | [`reference/`](reference/README.md) | Provenance: the three source curricula (preserved as PDFs) and how they map into the core. |

## How to read it

1. **Start with [PHILOSOPHY](PHILOSOPHY.md)** — it sets the lens (the
   goalkeeper as "soccer's great contrarian"; decision-making over
   reaction; eliminate danger before it happens).
2. **Place a keeper on the [development framework](framework/development-framework.md)** — find their stage (roughly U9–U12 foundation / U13–U15 development / U16–U18+ advanced) and what to emphasize.
3. **Train from the [syllabus](syllabus/README.md)** — each category is a
   self-contained technical reference.
4. **Run it with the [drills](drills/library.md)**, organized by the two
   training methods in [training-methodology](framework/training-methodology.md).
5. **Speak the [vocabulary](vocabulary.md)** — especially the four-stage
   [communication syllabus](framework/communication-syllabus.md).

## Shape + what's next

`shape_pattern` is **structural** — this v0.x ships the knowledge
foundation, not yet executable skills. A future **toolkit** layer (a
session-builder, a per-keeper development tracker, drill-selection skills)
would sit on top of this core, the same way the engineering domain's
skills sit on its rules. The core is deliberately stable: it is the
"foundational informational for everything going forward."

This file replaces the fork's `content/SHAPE.md`. The three source
curricula are **cited** under [`reference/`](reference/README.md) (see
[`reference/sources/SOURCES.md`](reference/sources/SOURCES.md)); the
copyrighted source PDFs are held locally by the maintainer and are **not
redistributed in this repository**.
