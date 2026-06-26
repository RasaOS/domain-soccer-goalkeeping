---
title: The 4-Stage Communication Syllabus
element: rasa.domain.soccer.goalkeeping
layer: core/framework
sources: [robo, ecnl, plan]
---

# The 4-Stage Communication Syllabus

The goalkeeper is the organizer of the defense. Both the ECNL Handbook and
the Goalkeeper Plan structure communication as a **four-stage developmental
progression** — what a keeper communicates escalates in scope as competence
grows, from claiming a single ball, to directing one teammate, to commanding
the back line, to running the whole team's tactical shape. The two sources
define the same four stages with the same command glossary (their definitions
are near-identical and are merged below). Robo ("The GK Trainer") does not lay
out a four-stage system, but contributes the `KEEPER!` command and the
"can I win the ball?" decision-making that grounds Stage One; where Robo's
framing adds something, it is noted.

This file is the command-vocabulary reference. For the mentality that makes a
keeper willing to command — bravery, decisiveness, "never a cheerleader" — see
[psychology-mentality](../syllabus/psychology-mentality.md). For the
situations these commands organize (corners, free kicks, breakaways), see
[aerial-crosses](../syllabus/aerial-crosses.md) and
[one-v-one-breakaway](../syllabus/one-v-one-breakaway.md). Every command term
is also listed in the [glossary](../vocabulary.md).

> **Note on source paths:** The canonical syllabus filenames live in the
> sibling `syllabus/` directory; this framework file cross-references them by
> the architecture's exact filenames.

---

## Qualities of Effective Communication

Five principles govern every call, regardless of stage (ECNL + Plan, stated
identically in both):

- **Loud, clear, and concise.** A command that isn't heard, isn't understood,
  or buries the instruction in extra words is not communication. Strip it to
  the essential information.
- **Tone carries urgency or calm.** Goalkeepers use their **tone** to express
  urgency or calmness while reading the situation. A louder voice expresses
  more urgency (e.g. a shouted `PUSH UP` vs. a measured one). The keeper
  modulates volume and pitch deliberately — the *word* tells the teammate
  *what*; the *tone* tells them *how urgently*.
- **Goalkeepers are always in control.** The call is an act of command. An
  effective call not only communicates to teammates but shows the keeper is
  in control of the game — and, on a claim, tells opponents the ball belongs
  to the goalkeeper.
- **Never a cheerleader.** *"A goalkeeper is never a cheerleader and should
  deliver helpful information without merely shouting common terms."* Empty
  noise — "let's go," "heads up," generic encouragement — is not
  communication. Every call must carry actionable information. If it doesn't
  change what a teammate does, don't say it.
- **Communication assists attack, not just defense.** Effective communication
  will not simply address the defenders — it may also assist in attacking
  moves (the entire premise of Stage Four).

Underneath all of it sits the ECNL proactivity principle: *"You eliminate the
danger before it happens. If you only react, then you have to make a save."*
Communication is the keeper's primary tool for **eliminating danger before it
happens** — organizing pressure, cover, and shape so the dangerous moment
never arrives. A keeper who only reacts has already conceded the initiative.

---

## Stage One — Confident on Own Saves / Claim the Ball

**Purpose.** The foundation. Before a keeper can direct anyone else, they must
be **confident in making a save and in control of the situation**. Stage One
is about the keeper and the ball: claim it or release it, every single time,
out loud. An effective call at this level does three things at once — it
communicates to teammates, it shows the keeper is in control of the game, and
it tells the **opponents** the ball belongs to the goalkeeper.

This stage is the developmental floor: confidence and command come first, and
the tactical sophistication of Stages Two through Four is layered on top of it.

**Command vocabulary.**

| Command | Meaning |
|---|---|
| **KEEPER** | Called every time the keeper *can* make the save or handle the ball. Claims the ball for the keeper. **Always two syllables** — never allow the keeper to simply yell "Keep." |
| **AWAY** | Called every time the keeper *cannot* make the save, or wants a teammate to control/clear the ball. Releases the ball to the teammate. |

**The non-negotiable rule (ECNL + Plan):** on every set piece — indeed on
every ball into the area — the keeper claims or releases verbally: **`KEEPER`
or `AWAY`, no matter what, every single time.** This includes balls that fly
well over the goal. There is no such thing as a ball the keeper lets pass in
silence. The habit of always calling removes the catastrophic ambiguity where
keeper and defender both leave it, or both go for it.

**Robo's contribution.** Robo independently establishes `KEEPER!` as the call
a goalkeeper makes when deciding to come win a ball: *"a command of courtesy
and tactics."* It is **courtesy** because it lets teammates take up cover
positions behind the advancing keeper; it is **tactics** because it warns
opponents a physical challenge is coming. Robo also supplies the decision that
sits behind the call — **"Can I win the ball?"** — weighed against the total
distance to travel, whether a teammate is closer, and whether opponents or
teammates obstruct the path. "Can I win the ball?" is framed as *a
consideration, not a commandment*. (Full treatment in
[positioning-angles](../syllabus/positioning-angles.md) and
[aerial-crosses](../syllabus/aerial-crosses.md).)

---

## Stage Two — Connect With Individual Teammates

**Purpose.** One-to-one commands. Stage Two is how the goalkeeper connects
with the **individual** teammates defending or advancing the ball — directing
a single named player, not the group. Calls are typically prefixed with the
player's **name** so the instruction lands on exactly one teammate.

**Command vocabulary.**

| Command | Meaning |
|---|---|
| **(NAME) STEP / PRESSURE** | Tells an individual to put pressure on the ball — prevent the attacker from advancing further or shooting. Used when there is **space** between the defender and the attacker. |
| **FORCE LEFT / FORCE RIGHT** | Tells a *pressuring* defender which way to push/force the opponent. **Left/Right is preferred to Inside/Outside** unless the ball is extremely wide. Used when the defender is **close** to the attacker. |
| **(NAME) DROP** | Tells an individual to run back to a more defensive position. (May also be used to address the entire team.) |
| **TURN (LEFT/RIGHT)** | Lets a teammate know they have **time to turn** with the ball. Adding a direction speeds up play — it tells the player which side of the field to face. |
| **TIME** | Tells a teammate there is **little pressure** on the ball and they have time to play it with their feet. |
| **MAN ON** | Tells a teammate they are under pressure, or about to be. Emphasize **urgency** in the tone. |
| **(KEEPER'S) HOME** | Tells a teammate to play the ball **back to the goalkeeper** (invites the back-pass that starts build-up). |

**Pairing logic:** `STEP/PRESSURE` and `FORCE LEFT/RIGHT` work as a sequence —
first send the defender to pressure when there's space, then steer the
direction of that pressure once the defender is tight to the attacker. `TIME`
and `MAN ON` are opposites the keeper calls based on what they can see that the
teammate (whose back is turned) cannot.

---

## Stage Three — Organize the Functional Group / Back Line

**Purpose.** Group command. Stage Three is how the keeper communicates to an
entire **functional group** of defenders — most usually the **back four**.
The keeper is now moving the line as a unit, setting the defensive shape, and
organizing marking and walls on set pieces. From here on the keeper is
genuinely **running the defense**, not just nudging individuals.

**Command vocabulary.**

| Command | Meaning |
|---|---|
| **OPEN UP** | Tells a teammate to take an "open" body position to see as much of the field as possible. Used when the ball is played **wide**. |
| **DROP BACK** | Makes the **entire back line** aware they need to run back, more defensively, **quickly**. |
| **PUSH UP** | Tells the entire defense to move up the field **in unison**. A **louder voice expresses more urgency**. |
| **HOLD** | Sets/keeps the defensive line. Defenders do not stand behind a certain **line / spot / named** defender — giving the keeper more control of the space behind the back line. On free kicks it may also be used to create an **offside trap**. Forms: `HOLD (LINE / SPOT / NAME)`. |
| **CONTAIN / DELAY** | Tells a teammate to stay in front of the ball and **slow the attacker** so other players can recover to help. Often paired with terms addressing the recovering players. |
| **DOUBLE TEAM** | Tells a **second** defender to step to the ball to make it harder to penetrate. Used when defenders **outnumber** attackers and there is proper cover. |
| **(NAME) COVER** | Tells a teammate to drop **behind** another defender to help cover. Used alongside a command to the first defender. |
| **KEEP OUTSIDE** | When the ball is wide, signals the defender to use **body shape** to keep the ball wide / force it to be played negatively. |
| **WALL (#)** | Form a wall with the stated **number** of players, **ten yards** from goal. The keeper then **moves the wall** into the right position. |
| **(NAME) MARK (#)** | Tells a specific player to **mark** a specific opponent. |
| **GOAL SIDE** | Tells a player to defend **tightly** and stay on the **goal-side** of their mark. Used when defending free kicks, alongside marking instructions. |

**Set-piece grouping:** `WALL (#)`, `HOLD`, `(NAME) MARK (#)`, and `GOAL SIDE`
are the keeper's free-kick and corner organizing kit — number the wall, set the
line, assign the marks, and demand goal-side positioning. `WALL (#)` connects
directly to the wall-size decision (how many players by zone) covered in
[aerial-crosses](../syllabus/aerial-crosses.md) and the
[drill library](../drills/library.md). `DROP BACK` / `PUSH UP` are the unison
line commands; `CONTAIN/DELAY`, `DOUBLE TEAM`, and `(NAME) COVER` form the
pressure-cover-balance trio for live defending.

---

## Stage Four — Advanced Tactical Instruction to the Whole Team

**Purpose.** Whole-team command. Stage Four is the keeper communicating
**advanced tactical instructions to the entire team** — attacking and
transition organization, not just defending. This is where the principle
"communication assists attack" is fully realized: the keeper is now shaping
the point of attack, organizing transition, and directing recovery across the
full field.

**Command vocabulary.**

| Command | Meaning |
|---|---|
| **(NAME) IS ON** | Tells an attacker (the player on the ball) that a certain teammate is **able to receive a pass**. |
| **SWITCH** | **Quickly send the ball** to a player on the other side of the field. |
| **SWING** | Drop the ball to a player so they may send it to the other side — and tells the **opposite-side** player to **get wide** as well. |
| **(NAME) TUCK IN** | Tells a defender (or group) to fall in more **centrally** and defend more toward the goal. |
| **(NAME) RECOVER CENTRAL** | In a **crossing** situation, tells a defender to run to the **center** of the field to defend the ball. |
| **(NAME) BACK POST** | Tells a specific player to recover to the **back post** to mark a **weak-side** attacker running down the field. |
| **INTO TOUCH** | Used when the defense is **not in position** to build a counter or play out of the back. Express **urgency** — clear it out of bounds — then follow with instructions to the entire defense. |
| **SHIFT (RIGHT/LEFT)** | Gets the **entire team** to move its defensive shape toward the ball on one side, following the attacking team **switching/swinging** the point of attack. |

**Attack vs. recovery split:** `(NAME) IS ON`, `SWITCH`, and `SWING` are the
attacking/build-up calls — the keeper using their full view of the field to
move the ball to space. `TUCK IN`, `RECOVER CENTRAL`, `BACK POST`, and
`SHIFT (RIGHT/LEFT)` are the transition/recovery calls — reorganizing the
team's shape as the attack moves. `INTO TOUCH` is the safety valve when build-up
is impossible. `SWITCH` / `SWING` / `INTO TOUCH` also drive distribution
decisions — see [distribution](../syllabus/distribution.md) and
[playing-with-feet](../syllabus/playing-with-feet.md).

---

## Full Command Glossary (Quick Reference)

All command terms, grouped by stage. Source: ECNL Handbook + Goalkeeper Plan
(identical glossaries), plus Robo for `KEEPER!`.

**Stage One — claim/release**
`KEEPER` · `AWAY`

**Stage Two — individual teammate**
`(NAME) STEP/PRESSURE` · `FORCE LEFT / FORCE RIGHT` · `(NAME) DROP` ·
`TURN (LEFT/RIGHT)` · `TIME` · `MAN ON` · `(KEEPER'S) HOME`

**Stage Three — functional group / back four**
`OPEN UP` · `DROP BACK` · `PUSH UP` · `HOLD (LINE/SPOT/NAME)` ·
`CONTAIN/DELAY` · `DOUBLE TEAM` · `(NAME) COVER` · `KEEP OUTSIDE` ·
`WALL (#)` · `(NAME) MARK (#)` · `GOAL SIDE`

**Stage Four — whole team / advanced tactics**
`(NAME) IS ON` · `SWITCH` · `SWING` · `(NAME) TUCK IN` ·
`(NAME) RECOVER CENTRAL` · `(NAME) BACK POST` · `INTO TOUCH` ·
`SHIFT (RIGHT/LEFT)`

---

## Coaching Notes

- **Teach the stages in order.** A keeper who cannot yet command their own
  six-yard box (Stage One) should not be drilled on `SWITCH` and `SHIFT`
  (Stage Four). Confidence claiming the ball is the prerequisite; the rest is
  built on top.
- **Two syllables, always.** The single most-repeated mechanical rule across
  both sources: `KEEPER` is two syllables. Never let it collapse into "Keep."
  The extra syllable is what carries over the noise of a game.
- **Every ball gets a call.** `KEEPER` or `AWAY`, no matter what — including
  balls flying well over the bar. The discipline of always calling is what
  eliminates the both-go / both-leave disasters.
- **Tone is half the message.** Same word, different urgency, depending on
  volume and pitch. The keeper who barks `MAN ON` and murmurs `TIME` is
  reading the game *for* their teammates whose backs are turned.
- **Name the player.** Most Stage Two–Four commands are name-prefixed for a
  reason: an unaddressed instruction lands on no one. `(NAME)` makes it
  unambiguous who must act.

---

## Sources

- **Robo** — "The GK Trainer" (Rob Walker, US National Goalkeeping Staff
  Coach): contributes the `KEEPER!` command as "a command of courtesy and
  tactics," and the "Can I win the ball?" decision-making that grounds Stage
  One. Robo does not define a four-stage system.
- **ECNL** — "ECNL Goalkeeping Curriculum & Handbook," First Edition (BUSA):
  defines the four-stage communication syllabus, the Qualities of Effective
  Communication (loud/clear/concise, tone, "never a cheerleader," "eliminate
  the danger before it happens"), and the full command glossary. Primary
  source for this file.
- **Plan** — "Goalkeeper Plan 2015-2016": defines the same four-stage syllabus
  and an identical command glossary; reinforces the loud/clear/concise and
  "never a cheerleader" principles and the two-syllable `KEEPER` rule.
  Communication appears in its age-band syllabus as "Communication" (U13-U15)
  and "Advanced Communication" (U16-U18).
