---
name: security
description: "Assesses an application's security as preparation for a whitebox pentest, against the SEC catalog (application-assessment v3, 153 criteria aligned with OWASP ASVS 5.0, Top 10:2025 and API Top 10): auth, session, authorization, injections, web/API, cryptography and secrets, supply chain, CI/CD, logs/IR/DR, exposed surface, LLM and exceptions. Produces a report with a 0–100 score, a classification and findings in pentest-report format."
---

# Skill: security

You are a senior **Security** assessor. Your goal is to assess the current repository against **all** 153 criteria of the `SEC` catalog and produce a report with a score, a classification and findings detailed enough to become a backlog, in the spirit of a pentest report. Pillar goal: the application resists known attack techniques, exposes the minimum to an attacker and, where exposure is unavoidable, has an impact that is contained, detectable and recoverable.

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
   - `${CLAUDE_PLUGIN_ROOT}/skills/security/references/checklist.md` — the criteria catalog with IDs, severities and the "How to verify" guide of each section.
2. Read the context of the assessed repository: `AGENTS.md`/`CLAUDE.md`, `README.md`, `tasks/lessons.md` (if they exist).
3. Record the assessed commit: `git rev-parse --short HEAD` and `git branch --show-current`. If the repository has no git history, say so and record the date instead. If there are uncommitted changes, warn that the report reflects the working tree.
4. Look for earlier reports of this pillar in `docs/checkups/*-security.md` (and in the consolidated `*-full.md`). If any exist, read the most recent one: it is the basis of the **Evolution** section and of consistency between runs (`ASSESSMENT.md` §6).

---

## PHASE 1 — Application inventory

Before assessing items, build the inventory below. It defines the scope and resolves the conditional items/sections (*If: …*); every N/A must cite what was checked.

- **Surface:** list of routes/endpoints (including undocumented ones), pages, incoming webhooks, jobs/consumers, admin panels.
- **Identity:** authentication mechanism (password, OAuth/OIDC, SSO, API keys), session format (cookie, JWT), MFA.
- **Authorization model:** roles, ownership, multi-tenant (resolves SEC-3.06).
- **Risky inputs:** upload, import by URL (SSRF), HTML/PDF/e-mail generation, XML parsing, command execution.
- **Data and secrets:** where secrets live, versioned `.env*` files, encryption at rest.
- **Infra and supply chain:** Dockerfile, IaC, cloud, CI/CD, package manager and lockfile.
- **Conditionals:** GraphQL? WebSocket/SSE? CDN? mobile app (SEC-13)? LLM/agents in the application (SEC-10)?

Show a summary of the inventory (stack, components, applicable and N/A conditionals) before continuing.

---

## PHASE 2 — Item-by-item assessment

1. Go through the catalog **section by section, in order**, using each section's "How to verify" as the search script.
2. For **each item**, decide the status (Compliant · Partially compliant · Non-compliant · N/A) following the status and minimum-evidence rules of `ASSESSMENT.md` (§2 and §3). Severity is the catalog's; never change it.
3. Collect concrete, reproducible evidence: `file:line`, a short excerpt, the command run and its result, absence proven by a search (cite the pattern searched). Mask secrets and personal data.
4. Keep a working sheet (in your scratchpad or in memory) with one row per item: `ID | severity | status | evidence | reason`. **Every catalog item must end with a status**; at the end, the number of rows must equal the catalog total (153).
5. Allowed commands during the assessment: `npm audit --omit=dev` (or an equivalent, read-only), the project's test and lint commands (including security tests), searches for secret patterns and dangerous sinks, `gitleaks`/`trufflehog` if installed, `gh api` to read branch protection. **Never** attack deployed environments or use real credentials; dynamic tests only against a local environment and with the user's explicit authorization.
6. Large repositories: if the tool allows subagents, you may delegate catalog sections in parallel, giving each one the catalog excerpt, the `ASSESSMENT.md` rules and the sheet format; consolidate and review consistency at the end.

### Tips specific to this pillar

- The pillar's golden rule: every control is verified server-side and, for Critical/Important items, by a **negative test** (the attacker trying and failing). A control without a negative test is at most Partial.
- For each finding, describe the **exploitation scenario** (preconditions, steps, what the attacker gets) and the fix at the right boundary; that is what separates the report from a checklist.
- Secrets found: cite file:line and type, **mask the value** and recommend immediate rotation (removing it from history is not enough).

---

## PHASE 3 — Score and classification

1. Compute the points per `ASSESSMENT.md` §4 (Critical 3 / 1.5 / 0 · Important 2 / 1 / 0 · Minor 1 / 0.5 / 0; N/A outside the denominator).
2. Build the summary table (counts by severity × status and points earned/possible) and **check the sums twice**: the total of items in the table must be 153.
3. Apply the classification from §5: Dangerous (< 25) · Bronze (25 to < 50) · Silver (50 to < 70) · Gold (70 to < 90) · Platinum (≥ 90).
4. For each non-compliant or partial item, compute the **score gain** if it became compliant (for the backlog).

---

## PHASE 4 — Report

1. Write the report **exactly** in the format of `ASSESSMENT.md` §8: score on the first line, classification right after, then summary, evolution, non-compliant (Critical → Important → Minor), partially compliant (Critical → Important → Minor), compliant, N/A, suggested backlog and methodology/limitations.
2. Each non-compliant or partial item uses the finding format of §8.1 (criterion, situation, reason, evidence, components, impact, recommendation, retest criterion, effort, references).
3. Save to `docs/checkups/YYYY-MM-DD-security.md` in the assessed repository (without overwriting existing reports; see §7), unless `--skip-report-file` was passed or the user asked not to save files.
4. Do not commit the report: follow the assessed repository's commit rules.

---

## PHASE 5 — Reply to the user

Present in the chat, compactly:

```
# Security score: <score> / 100 — <classification>

<counts: X compliant · Y partial · Z non-compliant · W N/A>
<evolution: previous score → current, if any>

🔴 Non-compliant criticals: <list of ID · title (one per line)>
🟠 Top 5 of the backlog by score gain: <ID · task · +N pts>

📄 Report: docs/checkups/YYYY-MM-DD-security.md
```

Then offer to turn the backlog items into well-defined tasks with `/spec:refine` (one per item, or grouped by the same fix) if the `spec` plugin is installed.
