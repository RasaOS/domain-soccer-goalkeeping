#!/usr/bin/env python3
"""
enforce-output-style.py — Stop hook that enforces the project's response
format contract (the "hard" layer of the RasaOS 3-layer output-style model).

WHAT IT DOES
  When Claude finishes a turn, this hook inspects Claude's last text response
  and checks it against a small, machine-checkable contract. If the response
  violates the contract, the hook BLOCKS the stop and hands Claude a reason —
  Claude reformats and tries again (once per turn).

THREE-LAYER MODEL  (see content/output-style-enforcement/README.md)
  1. soft   — the output style at .claude/output-styles/rasa-default.md
              (select it with /output-style; it modifies the system prompt).
  2. medium — the pointer in CLAUDE.md keeping the rule in context.
  3. hard   — THIS hook. Off by default; opt-in per session.

TOGGLE  (per session)
  ON : cp .claude/output-style.enforce.example.json .claude/output-style.enforce.json
  OFF: rm .claude/output-style.enforce.json
  The hook is a no-op whenever that file is absent or has "enabled": false,
  so it is safe to leave wired in settings.json permanently.

WIRING  (one-time)
  Merge content/output-style-enforcement/settings.snippet.json into
  .claude/settings.json (or settings.local.json).

HONEST LIMITATION
  A Stop hook cannot rewrite prose or judge nuanced style. It can only check
  the *structurally checkable* subset of a format (presence/absence of regex
  markers, minimum length). Put the full human-readable format in the output
  style; put the checkable markers in the config below.

CONFIG  (.claude/output-style.enforce.json)
  {
    "enabled": true,
    "min_chars": 400,               # below this length, don't enforce (no nag on short replies)
    "must_contain": ["regex", ...], # ALL of these must match the response
    "must_not_contain": ["regex"],  # NONE of these may match
    "skip_if_matches": ["regex"],   # if ANY matches, skip this response entirely
    "message": "..."                # shown to Claude when a check fails
  }

SAFETY
  This hook never silently breaks a session: missing/disabled config, bad JSON,
  or an unreadable transcript all result in exit 0 (allow the stop). A *malformed
  regex in the config* is surfaced as a visible failure (one block, naming the
  offending pattern) rather than silently disabling the check — a disabled check
  would give a false sense of enforcement. It blocks at most once per turn
  (honors stop_hook_active), so a mis-written check cannot trap Claude in a loop.
"""
import json
import os
import re
import sys


def load_stdin():
    try:
        return json.loads(sys.stdin.read() or "{}")
    except Exception:
        return {}


def project_dir(data):
    return data.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()


def last_assistant_text(transcript_path):
    """Joined text of the last assistant message in the JSONL transcript."""
    text = ""
    try:
        with open(transcript_path) as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except Exception:
                    continue
                if obj.get("type") != "assistant":
                    continue
                content = (obj.get("message") or {}).get("content")
                parts = []
                if isinstance(content, list):
                    for item in content:
                        if isinstance(item, dict) and item.get("type") == "text":
                            parts.append(item.get("text", ""))
                elif isinstance(content, str):
                    parts.append(content)
                joined = "".join(parts).strip()
                if joined:
                    text = joined  # keep the last non-empty assistant text
    except Exception:
        return ""
    return text


def allow():
    sys.exit(0)


def block(reason):
    print(json.dumps({"decision": "block", "reason": reason}))
    sys.exit(0)


def main():
    data = load_stdin()

    # Already nudged once this turn — don't loop. Allow the stop.
    if data.get("stop_hook_active"):
        allow()

    cfg_path = os.path.join(project_dir(data), ".claude", "output-style.enforce.json")
    if not os.path.isfile(cfg_path):
        allow()  # OFF — feature not toggled on for this session

    try:
        cfg = json.load(open(cfg_path))
    except Exception:
        allow()  # bad config → never break the session
    if not cfg.get("enabled", False):
        allow()

    transcript = data.get("transcript_path")
    if not transcript or not os.path.isfile(transcript):
        allow()
    text = last_assistant_text(transcript)
    if not text:
        allow()

    if len(text) < int(cfg.get("min_chars", 0)):
        allow()
    for pat in cfg.get("skip_if_matches", []):
        try:
            if re.search(pat, text):
                allow()
        except re.error:
            continue

    failures = []
    for pat in cfg.get("must_contain", []):
        try:
            if not re.search(pat, text):
                failures.append("missing required pattern: %s" % pat)
        except re.error as exc:
            # Surface a broken config regex loudly — silently skipping it
            # would give a false sense of enforcement.
            failures.append(
                "invalid must_contain regex %r (%s) — fix .claude/output-style.enforce.json"
                % (pat, exc))
    for pat in cfg.get("must_not_contain", []):
        try:
            if re.search(pat, text):
                failures.append("contains forbidden pattern: %s" % pat)
        except re.error as exc:
            failures.append(
                "invalid must_not_contain regex %r (%s) — fix .claude/output-style.enforce.json"
                % (pat, exc))

    if not failures:
        allow()

    msg = cfg.get(
        "message",
        "Your last response did not follow the required format in "
        ".claude/output-styles/rasa-default.md. Reformat and resend.",
    )
    block(msg + "\n\nFailed checks:\n- " + "\n- ".join(failures))


if __name__ == "__main__":
    main()
