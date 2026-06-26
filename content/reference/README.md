---
title: Reference & Provenance
element: rasa.domain.soccer.goalkeeping
layer: core/reference
---

# Reference & Provenance

The domain core is **synthesized from three real goalkeeping curricula**.
Those source documents are **cited** here (see
[`sources/SOURCES.md`](sources/SOURCES.md)); the source PDFs themselves are
third-party copyrighted and are **not redistributed in this repository** —
they are held locally by the maintainer. Everything in
[`../syllabus/`](../syllabus/README.md),
[`../framework/`](../framework/README.md),
[`../drills/library.md`](../drills/library.md),
[`../vocabulary.md`](../vocabulary.md), and
[`../PHILOSOPHY.md`](../PHILOSOPHY.md) traces back to these documents. When
the core and a source disagree, **the source is the ground truth**.

## The sources

Full citations in [`sources/SOURCES.md`](sources/SOURCES.md). At a glance:

| # | Document | Author / org | What it anchors |
|---|---|---|---|
| 1 | *Developing a Training Program for Coaching Goalkeeping* ("The GK Trainer") | **Rob Walker**, US National Goalkeeping Staff Coach | The deep **technical** curriculum — catching, footwork, diving, high balls/crosses, 1v1, distribution, positioning; the two training methods; the U12–U19 load bands. |
| 2 | *ECNL Goalkeeping Curriculum & Handbook*, First Edition | **Birmingham United Soccer Association (BUSA)**, ECNL program | The **philosophy** ("goalkeepers are soccer's great contrarians"), the **four-stage communication** syllabus, tactical situations (crosses/corners, 1v1, through-balls) via field diagrams, and **mentality**. |
| 3 | *Goalkeeper Plan 2015–2016* | Youth club GK program | The most complete **program**: organization, the U9–U18 age syllabus (Fall & Spring, Aug–May), the **named drill library** (Stalk, Steal Ground, Power Step, Collapse/Step/Extension dives, Basket/Scoop/Contour catches…), the four-stage communication curriculum, and **testing** per band. |

## How they map into the core

- **PHILOSOPHY** ← ECNL (identity, bravery, decision-making) + Robo (long-term development, essentials-first, hold-and-react).
- **framework/development-framework** ← Robo age bands (U12–U19) + Plan age bands (U9–U18) + "Testing."
- **framework/training-methodology** ← Robo + Plan (Simple-to-Complex, Whole-Part-Whole, session structure, organization, charting).
- **framework/communication-syllabus** ← ECNL + Plan (the four stages + command glossary).
- **syllabus/** (9 categories) ← Robo (richest technical detail) + ECNL (tactical situations) + Plan (drills + footskills + fitness).
- **drills/library** ← Plan (named drills) + Robo (technique-implied exercises).
- **vocabulary** ← all three (Robo technique terms + ECNL/Plan command terms, deduped).

## A note on synthesis

The core **reorganizes and merges** these sources into a single coaching
reference; it does not invent technique or drills beyond what the sources
contain. Specific cues, age bands, numbers, and terminology are kept
faithful to the originals. Where only one source covers a topic — or where
two differ — the core says so.

The source PDFs are **not in this repository** — they are third-party
copyrighted coaching documents, held locally by the maintainer and cited
(not redistributed) per [`sources/SOURCES.md`](sources/SOURCES.md). The
Element's content is the synthesized core; the PDFs are the working source
of record on the maintainer's machine (gitignored under
`sources/`). The core itself is not auto-installed from here either — see
the install map in [`../README.md`](../README.md).
