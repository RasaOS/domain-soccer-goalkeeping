# Output-style enforcement

A reusable, three-layer pattern for enforcing a consistent **response format**
on every Claude session in a project. Ships in `rasa.domain.core`; every domain
Element that forks the template inherits it. Softest to hardest:

| Layer | What | Where it lives | Strength |
|-------|------|----------------|----------|
| 1 — soft | **Output style** — the format spec, injected into the system prompt | `.claude/output-styles/rasa-default.md` | Reliable, always-on once selected. Instruction-following, not mechanical. |
| 2 — medium | **CLAUDE.md pointer** — keeps the rule in context even when the style isn't the active one | the project `CLAUDE.md` "Response formatting" section | Defends against drift on long sessions. |
| 3 — hard | **Stop hook** — validates each finished response and bounces non-conforming ones back | `.claude/hooks/enforce-output-style.py` + `.claude/output-style.enforce.json` | Mechanical, per-session toggle. Enforces only the *checkable* subset. |

The honest ceiling: **no Claude Code mechanism rewrites your prose.** Layers 1–2
are instructions Claude follows; layer 3 is the only mechanical check, and it can
only verify *structurally checkable* rules (regex markers, minimum length) — not
nuanced style. Put the full human-readable format in the output style; put the
machine-checkable markers in the hook config.

---

## What gets installed

`bin/init` installs these into a consumer project (all **inert** until you act):

- `.claude/output-styles/rasa-default.md` — the format spec (seeded once;
  `skip-if-exists`; **you own it** — edit freely).
- `.claude/hooks/enforce-output-style.py` — the Stop hook (Element-owned code;
  refreshed on Element upgrade). Does nothing until wired **and** toggled on.
- `.claude/output-style.enforce.example.json` — the toggle template + example
  checks.

Not installed (fork-time docs): this `README.md` and `settings.snippet.json`.

---

## Turn it on

### Layer 1 — soft (recommended default)

Select the output style:

```sh
/output-style rasa-default
```

…or set it in `.claude/settings.json`:

```json
{ "outputStyle": "RasaOS Default" }
```

The style uses `keep-coding-instructions: true`, so it *adds* the format rules
on top of Claude Code's normal behavior rather than replacing them. Takes effect
on `/clear` or next session.

### Layer 3 — hard (per-session, opt-in)

1. **Wire it once.** Merge `settings.snippet.json` into `.claude/settings.json`
   (or `.claude/settings.local.json`).
2. **Toggle on for the session:**
   ```sh
   cp .claude/output-style.enforce.example.json .claude/output-style.enforce.json
   ```
3. **Toggle off:**
   ```sh
   rm .claude/output-style.enforce.json
   ```

When on, the hook checks each finished response; if it fails a check it blocks
the stop once and tells Claude to reformat. It blocks at most once per turn, so a
bad check can never trap a session. Consider adding `.claude/output-style.enforce.json`
to `.gitignore` if you want the toggle to stay machine-local.

> **Why a file, not an env var?** Hooks inherit the env of the Claude Code
> process that was running when it launched — an `export` in another terminal
> won't reach it. A sentinel file is the reliable mid-session toggle.

---

## Customize

- **The format** → edit `.claude/output-styles/rasa-default.md`. This is the
  source of truth a fork replaces with its own house style.
- **The machine checks** → edit `.claude/output-style.enforce.json`:

  | Key | Meaning |
  |-----|---------|
  | `enabled` | Master switch. `false` = no-op even if the file exists. |
  | `min_chars` | Responses shorter than this are never enforced. |
  | `must_contain` | List of regexes; **all** must match the response. |
  | `must_not_contain` | List of regexes; **none** may match. |
  | `skip_if_matches` | If **any** regex matches, skip this response. |
  | `message` | Shown to Claude when a check fails. |

  Keep the checkable markers here in sync with whatever in the output style is
  actually structural (e.g. "long responses carry a heading").

---

## Adopting in a fork

A fork of `rasa.domain.core` inherits this automatically. To tailor it:

1. Rewrite `seed/output-style.md.template` with your domain's house format.
2. Adjust `content/output-style-enforcement/output-style.enforce.example.json`
   so the checks match that format.
3. Leave the hook (`enforce-output-style.py`) as-is — it's generic.
