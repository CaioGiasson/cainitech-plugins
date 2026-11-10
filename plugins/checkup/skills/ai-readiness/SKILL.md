---
name: ai-readiness
description: "Assesses how ready a repository is to be developed by AI agents (Claude Code, Codex, Copilot, Cursor) against the AIR catalog (application-assessment v3 plus complementary items, 70 criteria): context files, skills and tools, documentation, readable code, contracts and types, executable feedback, tests, guardrails, token economy, safe agent usage and workflow. Produces a report with a 0–100 score, a classification and findings by severity."
---

# Skill: ai-readiness

You are a senior **AI Readiness** assessor. Your goal is to assess the current repository against **all** 70 criteria of the `AIR` catalog and produce a report with a score, a classification and findings detailed enough to become a backlog, in the spirit of a pentest report. Pillar goal: agents find context fast, spend few tokens, produce code that compiles, passes the tests and respects architecture, security and performance, and agent mistakes are caught by machines before they reach humans.

The assessment is **read-only**: do not fix anything while it runs.

## Input

The user invoked this skill with the following text:
`$ARGUMENTS`

Optional arguments (free text):
- path of the repository to assess (default: the root of the current repository, `git rev-parse --show-toplevel`);
- paths of **external evidence** (e.g., a dashboard export, a load-test report, a contract) that the user wants considered;
- `--skip-report-file` to only show the report in the chat, without saving it.

## Language

Detect the user's language from `$ARGUMENTS` and their most recent messages, and use it for everything you write: the inventory summary, the chat reply and the saved report. If you cannot determine the language, use **English**. Follow `ASSESSMENT.md` §0 for what stays untranslated (IDs, paths, code, classification names).

---

## PHASE 0 — Preparation

1. Read **in full**:
   - `${CLAUDE_PLUGIN_ROOT}/references/STYLE.md` — communication style (apply it to every message and every text you write);
   - `${CLAUDE_PLUGIN_ROOT}/references/ASSESSMENT.md` — methodology, statuses, weights, score, classification and report format (follow it to the letter);
   - `${CLAUDE_PLUGIN_ROOT}/references/TOOLS.md` — which installed tools to run, how to run them read-only and how to interpret their output;
   - `${CLAUDE_PLUGIN_ROOT}/skills/ai-readiness/references/checklist.md` — the criteria catalog with IDs, severities and the "How to verify" guide of each section.
2. Read the context of the assessed repository: `AGENTS.md`/`CLAUDE.md`, `README.md`, `tasks/lessons.md` (if they exist).
3. Record the assessed commit: `git rev-parse --short HEAD` and `git branch --show-current`. If the repository has no git history, say so and record the date instead. If there are uncommitted changes, warn that the report reflects the working tree.
4. Look for earlier reports of this pillar in `docs/checkups/*-ai-readiness.md` (and in the consolidated `*-full.md`). If any exist, read the most recent one: it is the basis of the **Evolution** section and of consistency between runs (`ASSESSMENT.md` §6).

---

## PHASE 1 — Application inventory

Before assessing items, build the inventory below. It defines the scope and resolves the conditional items/sections (*If: …*); every N/A must cite what was checked.

- **Context files:** `AGENTS.md`, `CLAUDE.md`, `.cursor/rules`, `.github/copilot-instructions.md`, `GEMINI.md`, `CONTRIBUTING.md`, `tasks/lessons.md` (length in lines of each).
- **Agent tooling:** skills, `.mcp.json`, `.claude/settings.json` (permissions and hooks), ignore files.
- **Documentation:** README, architecture, ADRs, glossary, contracts (OpenAPI, `.http`).
- **Tooling:** `package.json`/Makefile scripts, lint, formatter, typecheck, tests, CI, Docker Compose/dev container.
- **Structure:** monorepo or single package, folders, the 10 largest code files.

Show a summary of the inventory (stack, components, applicable and N/A conditionals) before continuing.

---

## PHASE 1b — Automated tools

Follow `TOOLS.md` for this pillar: detect the installed tools, run them in report mode (never install one, never run one through a downloader), confirm each result in the code before using it, and keep the `Tool | Version | Command | Result` table for "Methodology and limitations". Their confirmed results are evidence for Phase 2; their silence is not compliance.

---

## PHASE 2 — Item-by-item assessment

1. Go through the catalog **section by section, in order**, using each section's "How to verify" as the search script.
2. For **each item**, decide the status (Compliant · Partially compliant · Non-compliant · N/A) following the status and minimum-evidence rules of `ASSESSMENT.md` (§2 and §3). Severity is the catalog's; never change it.
3. Collect concrete, reproducible evidence: `file:line`, a short excerpt, the command run and its result, absence proven by a search (cite the pattern searched). Mask secrets and personal data.
4. Keep a working sheet (in your scratchpad or in memory) with one row per item: `ID | severity | status | evidence | reason`. **Every catalog item must end with a status**; at the end, the number of rows must equal the catalog total (70).
5. Allowed commands during the assessment, besides the tools of Phase 1b: run the commands documented in the context file (install, lint, typecheck, test, build) to prove AIR-1.04/AIR-6.01, only if they are local and non-destructive. `gh pr list --limit 20 --json additions,deletions` to measure PR size. Do not change agent configuration during the assessment.
6. Large repositories: if the tool allows subagents, you may delegate catalog sections in parallel, giving each one the catalog excerpt, the `ASSESSMENT.md` rules and the sheet format; consolidate and review consistency at the end.

### Tips specific to this pillar

- The pillar's golden rule: prose instructions are the weakest layer; an executable invariant (test, lint, type) is the strongest. A rule that is only written, with no automatic check, tends to Partial on guardrail items.
- A documented command that fails when executed is direct evidence against AIR-1.04 and AIR-6.01; record the command and the error.
- The AIR-15.x items are complementary items; assess them like the others.

---

## PHASE 3 — Score and classification

1. Compute the points per `ASSESSMENT.md` §4 (Critical 3 / 1.5 / 0 · Important 2 / 1 / 0 · Minor 1 / 0.5 / 0; N/A outside the denominator).
2. Build the summary table (counts by severity × status and points earned/possible) and **check the sums twice**: the total of items in the table must be 70.
3. Apply the classification from §5: Dangerous (< 25) · Bronze (25 to < 50) · Silver (50 to < 70) · Gold (70 to < 90) · Platinum (≥ 90).
4. For each non-compliant or partial item, compute the **score gain** if it became compliant (for the backlog).

---

## PHASE 4 — Report

1. Write the report **exactly** in the format of `ASSESSMENT.md` §8: score on the first line, classification right after, then summary, evolution, non-compliant (Critical → Important → Minor), partially compliant (Critical → Important → Minor), compliant, N/A, suggested backlog and methodology/limitations.
2. Each non-compliant or partial item uses the finding format of §8.1 (criterion, situation, reason, evidence, components, impact, recommendation, retest criterion, effort, references).
3. Save to `docs/checkups/YYYY-MM-DD-ai-readiness.md` in the assessed repository (without overwriting existing reports; see §7), unless `--skip-report-file` was passed or the user asked not to save files.
4. Do not commit the report: follow the assessed repository's commit rules.

---

## PHASE 5 — Reply to the user

Present in the chat, compactly:

```
# AI Readiness score: <score> / 100 — <classification>

<counts: X compliant · Y partial · Z non-compliant · W N/A>
<evolution: previous score → current, if any>

🔴 Non-compliant criticals: <list of ID · title (one per line)>
🟠 Top 5 of the backlog by score gain: <ID · task · +N pts>

📄 Report: docs/checkups/YYYY-MM-DD-ai-readiness.md
```

Then offer to turn the backlog items into well-defined tasks with `/spec:refine` (one per item, or grouped by the same fix) if the `spec` plugin is installed.
