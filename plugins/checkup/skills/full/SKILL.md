---
name: full
description: "Runs the complete assessment of an application across the four pillars (Performance, Security, Privacy/LGPD and AI Readiness) using the catalogs of the performance, security, privacy and ai-readiness skills (512 criteria). Produces the four per-pillar reports and a consolidated report with an overall 0–100 score, a classification (Dangerous to Platinum), cross-cutting risks and a single deduplicated backlog."
---

# Skill: full

You are the coordinator of a complete assessment. Your goal is to run the four pillars on the same commit, produce the four per-pillar reports and consolidate the result into an overall score and a single backlog.

The assessment is **read-only**: do not fix anything while it runs.

## Input

The user invoked this skill with the following text:
`$ARGUMENTS`

Optional arguments (free text):
- path of the repository (default: the root of the current repository);
- paths of external evidence to consider;
- list of pillars to skip (e.g., `without privacy`); skipped pillars are left out of the overall score and this shows in the report.

## Language

Detect the user's language from `$ARGUMENTS` and their most recent messages, and use it for everything you write: the chat reply and every report. If you cannot determine the language, use **English**. Follow `ASSESSMENT.md` §0 for what stays untranslated (IDs, paths, code, classification names). Use the same language for all four per-pillar reports and the consolidated one.

---

## PHASE 0 — Common preparation

1. Read `${CLAUDE_PLUGIN_ROOT}/references/ASSESSMENT.md` in full (§9 covers the consolidated report) and `${CLAUDE_PLUGIN_ROOT}/references/STYLE.md` (communication style: apply it to every message and every text you write).
2. Record the assessed commit (`git rev-parse --short HEAD`, branch); **all pillars assess the same commit**. If the repository has no git history, say so and record the date instead. If there are uncommitted changes, warn the user.
3. Read the repository context (`AGENTS.md`/`CLAUDE.md`, `README.md`, `tasks/lessons.md`), then decide the execution mode once for the four pillars (`ASSESSMENT.md` §1, "Running the project's code") and give it to each pillar.
4. Look for earlier reports in `docs/checkups/` (per pillar and consolidated) for the Evolution section.
5. Build **a single inventory** of the application (stack, frontend, database, integrations, authentication, personal data, third parties, CI/CD, infrastructure, agent context files, AI usage); it is shared by the four pillars and avoids repeated work.
6. If the repository has `.checkup.json` at its root, read `${CLAUDE_PLUGIN_ROOT}/references/CONFIG.md`, validate the file once and give each pillar its own entries with the validation outcome and the applied exclusions. The consolidated report lists every entry, applied or rejected, in one Exceptions table.
7. Read `${CLAUDE_PLUGIN_ROOT}/references/TOOLS.md` and run each installed tool **once** (a tool such as `gitleaks` serves more than one pillar); give each pillar the results that concern it. Apply the exclusions of step 6 as `TOOLS.md` §1 says (never to secret scanners).

---

## PHASE 1 — Running the pillars

For each pillar, run the complete flow of the corresponding skill (its Phases 1 to 4), reusing the inventory, the validated `.checkup.json` entries and the tool results from Phase 0 instead of repeating its Phase 0 and Phase 1b. Each pillar report applies its own exceptions and lists them in its Exceptions section, so the pillar files and the consolidated report agree:

| Pillar | Skill | Catalog | Items |
|---|---|---|---:|
| Performance | `/checkup:performance` | `${CLAUDE_PLUGIN_ROOT}/skills/performance/references/checklist.md` | 163 |
| Security | `/checkup:security` | `${CLAUDE_PLUGIN_ROOT}/skills/security/references/checklist.md` | 153 |
| Privacy (LGPD) | `/checkup:privacy` | `${CLAUDE_PLUGIN_ROOT}/skills/privacy/references/checklist.md` | 126 |
| AI Readiness | `/checkup:ai-readiness` | `${CLAUDE_PLUGIN_ROOT}/skills/ai-readiness/references/checklist.md` | 70 |

- **Order.** Privacy depends on Security (`PRIV-12.01` uses the Security result), so Security always runs first. If the tool allows subagents, run Security, then Privacy, Performance and AI Readiness **in parallel**, one subagent per pillar, giving each one: the execution mode (`run` or `static`, decided once in Phase 0; a subagent cannot ask), the pillar's `SKILL.md`, the catalog path, the paths of `TOOLS.md` and, when there is a `.checkup.json`, `CONFIG.md`, the pillar's validated exceptions and the applied exclusions (Phase 0 step 6), the tool results that concern it (Phase 0 step 7), the Phase 0 inventory, the commit, the earlier reports of that pillar and, for Privacy, the Security report. Otherwise run them in sequence: Security → Privacy → Performance → AI Readiness.
- **Wait for every pillar.** Start the pillar subagents in the foreground, never in the background: put the parallel ones in a single message, so they still run at the same time, and do not end your turn while a pillar is running. The consolidation needs the four results, and a run that ends its turn early leaves no consolidated report (a non-interactive run stops the pillars still running).
- Each pillar saves its own report to `docs/checkups/YYYY-MM-DD-<pillar>.md` (see `ASSESSMENT.md` §7).
- Before consolidating, check that each pillar assessed **all** of its items (count equal to the table above) and that the point sums add up.

---

## PHASE 2 — Consolidation

1. **Overall score** = Σ points earned in the four pillars ÷ Σ possible points of the applicable items in the four pillars × 100 (one decimal place). Do **not** use the average of the pillar scores.
2. **Classification** of the overall score: Dangerous (< 25) · Bronze (25 to < 50) · Silver (50 to < 70) · Gold (70 to < 90) · Platinum (≥ 90).
3. **Cross-cutting risks:** identify findings that appear in more than one pillar and treat them as a single problem (e.g., PII in logs: SEC-6.08, PERF-2.14, PRIV-12.06; timeouts and limits: PERF-4.07, SEC-5.14; authorization tests: SEC-3.01, AIR-7.01).
4. **Consolidated backlog:** merge the pillars' backlogs, deduplicating tasks that solve more than one item; the "Score gain" column shows the gain in the **overall score**. Order by severity, status and effort (`ASSESSMENT.md` §8.2).

---

## PHASE 3 — Consolidated report

Save to `docs/checkups/YYYY-MM-DD-full.md`, with the **overall score on the first line** and the **classification right after** (translate the labels per the Language section):

````markdown
# Overall score: 58.2 / 100
## Classification: Silver

# Full assessment — <repository name>

| Field | Value |
|---|---|
| Date | YYYY-MM-DD |
| Assessed commit | `<sha>` (branch `<branch>`) |
| Pillars | Performance, Security, Privacy, AI Readiness |
| Previous run | <file and previous score, or "first run"> |

## Score by pillar

| Pillar | Score | Classification | Non-compliant criticals | Partial criticals | Points earned / possible | Report |
|---|---:|---|---:|---:|---:|---|
| Security | | | | | | [link](YYYY-MM-DD-security.md) |
| Privacy | | | | | | |
| Performance | | | | | | |
| AI Readiness | | | | | | |
| **Overall** | | | | | **X / Y** | |

## Executive summary
<5–10 lines: overall posture, biggest risks, what unlocks the next classification>

## Evolution
<overall and per-pillar score: previous → current; main improvements and regressions>

## Cross-cutting risks
<each risk: pillars and IDs involved, impact, single recommended fix>

## Non-compliant and partial items — Critical (all pillars)
<table: ID · item · pillar · status · reason in one line · link to the finding in the pillar report>

## Consolidated backlog
| Priority | Task | IDs solved | Severity | Effort | Overall score gain |

## Methodology and limitations
<what could not be verified, external evidence needed, skipped pillars>
````

The details of each finding (pentest format) stay in the per-pillar reports; the consolidated report references the IDs and links.

Do not commit the reports: follow the assessed repository's commit rules.

---

## PHASE 4 — Reply to the user

```
# Overall score: <score> / 100 — <classification>

Security <s> (<class>) · Privacy <s> (<class>) · Performance <s> (<class>) · AI Readiness <s> (<class>)
<evolution, if any>

🔴 Non-compliant criticals: <N> — <the 5 most relevant, one per line>
🔗 Cross-cutting risks: <short list>
🟠 Top 5 of the backlog by overall score gain: <task · IDs · +N pts>

📄 Reports: docs/checkups/YYYY-MM-DD-{full,security,privacy,performance,ai-readiness}.md
```

Then offer to turn the consolidated backlog into well-defined tasks with `/spec:refine` if the `spec` plugin is installed.
