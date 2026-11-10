<p align="right"><b>🇺🇸 English</b> · <a href="README.pt-BR.md">🇧🇷 Português</a></p>

<div align="center">

# Your Claude, with a team's way of working

**Three Claude plugins that teach it to work like an experienced team: from idea to task, from task to code, from code to review, a health check for your whole application, plus interface polish so the sites and web apps it builds stop looking AI-made. You ask in plain language. It delivers.**

<table>
<tr>
<td align="center" width="25%"><h3>3 plugins</h3>install only what you need<br><sub><a href="#skill-catalog">see catalog</a></sub></td>
<td align="center" width="25%"><h3>11 skills</h3>ready to use<br><sub><a href="#skill-catalog">see catalog</a></sub></td>
<td align="center" width="25%"><h3>512 criteria</h3>assessed in the full health check<br><sub><a href="#system-health-check">see details</a></sub></td>
<td align="center" width="25%"><h3>1 message</h3>to install, right in the chat<br><sub><a href="#how-to-install">see installation</a></sub></td>
</tr>
</table>

**[Value](#why-it-matters-for-the-business) · [Install](#how-to-install) · [Before and after](#before-and-after) · [Catalog](#skill-catalog) · [How to use](#how-to-use) · [Update](#how-to-update) · [FAQ](#faq) · [Limits](#what-these-plugins-do-not-do) · [Trust](#trust-and-quality) · [Privacy](#privacy)**

</div>

---

## Why it matters for the business

**Less rework, more predictable delivery, and risks found before they become incidents.** These plugins turn your team's way of working into something Claude repeats every day, for everyone.

| The everyday problem | What the plugins do | What changes for the business |
|---|---|---|
| Vague requests cause back-and-forth and rework | Turn loose ideas and conversations into complete tasks, with a goal, rules and a test script | Fewer questions halfway through and deliveries that are easier to estimate |
| Everyone works their own way | Everyone follows the same steps and the same quality standard | Predictable quality and faster onboarding of new people |
| Coding, testing and reviewing eats the team's time | Claude implements, writes tests, reviews itself and delivers a ready pull request | The team spends energy on decisions, not repetitive tasks |
| Security, performance and privacy (LGPD) risks show up late | Health checks with a 0 to 100 score and a prioritized problem list | You see risks before they become incidents and get an action plan in a clear order |
| Knowledge lives in a few people's heads | Every task is recorded in the project's own documentation, with or without a task board | Less dependence on key people |

**Who it's for:** managers and leaders who want predictability, product people who want well-defined tasks, and development teams who want more time for what matters.

**Fits the project you have:** it uses your GitHub task board when there is one, still works without GitHub, and falls back to a plain change log when the project has no version control. It answers in the language you write in.

## Before and after

<table>
<tr>
<th width="50%">Without these plugins</th>
<th width="50%">With these plugins</th>
</tr>
<tr>
<td valign="top">

> "We need a way to download the invoice."

One loose sentence. Everyone reads it differently, the developer asks questions for days, and the result depends on who picked up the task.

</td>
<td valign="top">

> A complete task: goal, rules, what to change, how to test — on your board and in your docs. Code ready for review and a test script in hand.

Claude studies the system, asks only what's missing and delivers to the team's standard.

</td>
</tr>
</table>

<sub>Illustrative example of the kind of result each skill produces.</sub>

**Same idea. Organized delivery, to the team's standard.**

## How to install

You don't need to learn commands. You need the **Claude app** (**Code** tab). If something else is missing, Claude tells you and guides you.

1. Open the Claude app and go to the **Code** tab.
2. Paste this message into the chat and send it:

   > Install the plugins from the marketplace CaioGiasson/cainitech-plugins: run `claude plugin marketplace add CaioGiasson/cainitech-plugins`, then `claude plugin install checkup@cainitech`, `claude plugin install spec@cainitech` and `claude plugin install polish@cainitech`, and tell me when it's done.

3. Wait for Claude to confirm and open a **new conversation**. The skills now show up when you type `/`.

One message. That's it. Want only the health checks, only the task workflow or only the interface rules? Ask for just `checkup`, `spec` or `polish`.

**Prefer clicking?** Once the marketplace is added (step 2), click the **+** button next to the prompt box, choose **Plugins** and then **Add plugin** to install, or **Manage plugins** to turn a plugin on or off, update it or remove it.

<sub>Prefer the terminal or VS Code? See the <a href="docs/TECHNICAL.md">technical documentation</a>.</sub>

## How to update

When a new version is released, open **+ → Plugins → Manage plugins**, choose the plugin and click **Update now**. Or send this to Claude in the **Code** tab:

> Update the cainitech plugins: run `claude plugin marketplace update cainitech`, then `claude plugin update checkup@cainitech`, `claude plugin update spec@cainitech` and `claude plugin update polish@cainitech`.

New skills and improvements arrive right away (start a new conversation to load them).

## How to use

In any conversation in the **Code** tab, type `/` and pick the skill from the list. Skills of a plugin appear as `/<plugin>:<skill>`. Then write what you need in plain language.

> `/spec:refine` I want customers to be able to download their invoice as a PDF on the payments screen.

More examples, with the interface skill:

| You type | What happens |
|---|---|
| `/polish:ui` | Audits the project: finds the design system, reviews the main screens and lists the improvements by impact. |
| `/polish:ui` my orders screen looks AI-made | Redesigns that screen, reusing the project's components. |
| `/polish:ui` landing page for a neighborhood bakery | Builds a new page from your brief. |
| `/polish:ui review` the pricing page | Only assesses and reports. Changes nothing. |
| `/polish:ui system` | Creates the design system if there is none, or tidies up the existing one. |

Or just describe what you want. Claude also suggests the right skill.

> The skills reply in the language you write in. If they can't tell, they use English.

## Skill catalog

Eleven skills in three plugins. Each one says what it does and what result you get.

| Plugin | Group | What it's for | Skills |
|---|---|---|---|
| **`spec`** | **[From idea to task](#from-idea-to-ready-task)** | Turn loose conversation into a clear, recorded task | `/spec:from-thread` · `/spec:refine` |
| **`spec`** | **[From code to delivery](#from-code-to-delivery)** | Build, review and finish | `/spec:build` · `/spec:review` · `/spec:approve` |
| **`checkup`** | **[System health check](#system-health-check)** | Measure project health, changing nothing | `/checkup:security` · `/checkup:performance` · `/checkup:privacy` · `/checkup:ai-readiness` · `/checkup:full` |
| **`polish`** | **[Interface polish](#interface-polish)** | Make sites and web apps stop looking AI-made, on a reusable design system | `/polish:ui` |

**A task's full path:** `/spec:from-thread` or `/spec:refine` → `/spec:build` → `/spec:review` → you test → `/spec:approve`.

### From idea to ready task

| Skill | What it does | What you get |
|---|---|---|
| **`/spec:from-thread`** | Reads an informal conversation (Slack thread link, Discord link or a `.md` file), drops the noise and separates decisions from doubts and opinions. | A refined task recorded in your project's docs and, if you have a GitHub task board, created there — with no jokes, slang or loose information. |
| **`/spec:refine`** | Takes an idea described in a few lines, studies the system, asks focused questions and details everything. | A complete task (goal, rules, what to change and how to test), clear enough for anyone to carry out. It is **always recorded in your project's documentation**; if there's a board, it is also created there, with one sub-task per system involved. |

### From code to delivery

| Skill | What it does | What you get |
|---|---|---|
| **`/spec:build`** | Takes a task, moves it on the board to "In progress" (if there is a board), builds the solution, writes the tests and reviews its own work. | On GitHub: a ready *pull request* with the code in organized steps and a test script for you to check. Without GitHub: organized local commits. Without version control: a change log file with a copy of every change. Add `dry-run` to see the plan without changing anything. |
| **`/spec:review`** | Reviews a change in an isolated subagent that sees only the change, never your conversation: checks that everything requested was done, runs the tests and analyzes code quality. Refuses to review when there is no task, refinement document or PR description with acceptance criteria to check against. | Review comments posted on the right spot in the code, after you choose what to post (without GitHub, the review comes in the chat). It only fixes something if you ask. Add `dry-run` to review from the diff without checking out, building or posting. |
| **`/spec:approve`** | Steps in after your manual tests and does the final review before wrapping up. | If all is well, it shows exactly what it will do and waits for your OK: on GitHub, a final comment, a "Reviewed" label and the delivery completed (*merge*), then a separate question before cleaning up the working copies; without GitHub, a local merge. Add `dry-run` to see the plan without changing anything, or `no-merge` to approve without delivering. If it finds a serious problem, it only tells you and touches nothing. |

### System health check

**They only read and assess. They change nothing in your project.** Each health check delivers a report with a **score from 0 to 100**, a **rating** and a **list of problems by priority**, ready to become an action plan. The report is saved in the assessed project's `docs/checkups` folder.

| Skill | What it assesses | Criteria | What you get |
|---|---|---:|---|
| **`/checkup:security`** | Security: login, data protection, known weaknesses, exposed secrets. Works as preparation for a penetration test. | 153 | A security score and weak points by severity. |
| **`/checkup:performance`** | Speed, ability to grow, stability and infrastructure costs. | 163 | Where the system is slow or expensive and what to prioritize. |
| **`/checkup:privacy`** | Compliance with Brazil's LGPD: consent, data subject rights, personal data retention. | 126 | Legal gaps, each tied to its article of the law. |
| **`/checkup:ai-readiness`** | How ready the project is to be developed with AI help: documentation, tests, organization. | 70 | What to improve so AI works faster and makes fewer mistakes. |
| **`/checkup:full`** | All four health checks at once. | 512 | The four reports plus an overall one, with a single score, risks that cut across areas and one list of priorities. |

How to read the score:

| Score | Rating |
|---|---|
| 90 to 100 | 🏆 Platinum |
| 70 to 89 | 🥇 Gold |
| 50 to 69 | 🥈 Silver |
| 25 to 49 | 🥉 Bronze |
| 0 to 24 | 🚨 Dangerous |

### Interface polish

**Rules only: it runs no commands and downloads nothing.** Neutral: it brings no brand, palette or framework of its own. It works through your project's design system: uses it when it is healthy, improves it when it is inconsistent, and creates a small one when there is none, so components are reused instead of re-invented on every screen.

| Skill | What it does | What you get |
|---|---|---|
| **`/polish:ui`** | Builds, redesigns or reviews websites and web app screens (landing pages, dashboards, tables, forms, settings). First it audits the design system, then it removes the visual and writing habits that give AI-made interfaces away, deciding each choice from your product instead of from the usual template. Just describe what you want; add `review` to only assess, or `system` to work on the design system alone. | An interface that reads as made for your product, built from shared tokens and components, plus a short report: what changed in the design system, why each main choice was made, what was assumed and what material you still need to supply. |

<sub>Site rules adapted from <a href="https://github.com/Leonxlnx/taste-skill">taste-skill</a> (MIT), without its scripts, hooks or downloads.</sub>

## What a health-check result looks like

An example **with made-up data** of `/checkup:security` run on a project called `loja-online`. This is the reply that appears in the chat; the full report is saved to a file.

```text
# Security score: 56.1 / 100 — Silver

63 compliant · 28 partial · 46 non-compliant · 16 N/A (153 criteria)
Evolution: first run

🔴 Non-compliant criticals (14):
  SEC-2.04 · Brute force, credential stuffing and rate-limit evasion
  SEC-2.05 · MFA
  SEC-2.08 · Recovery
  SEC-3.02 · BOLA/IDOR
  SEC-5.06 · XSS
  … and 9 more (full list in the report)
🟠 Top 5 of the backlog by score gain:
  SEC-3.02 · Check order ownership on every /orders route · +1.0 pt
  SEC-2.04 · Rate limit per account and per IP on login · +1.0 pt
  SEC-2.08 · Single-use, expiring password-recovery token · +1.0 pt
  SEC-2.05 · Offer MFA for administrative accounts · +1.0 pt
  SEC-5.06 · Sanitize the product comment field · +1.0 pt

📄 Report: docs/checkups/2026-10-14-security.md
```

In plain English: the project scored **56.1 out of 100 (Silver)**; 14 critical problems are open, and the list says which ones to fix first and how many points each fix is worth.

<details>
<summary><b>See an excerpt of the saved report</b></summary>

````markdown
# Score: 56.1 / 100
## Classification: Silver

# Security Assessment — loja-online

| Field | Value |
|---|---|
| Date | 2026-10-14 |
| Assessed commit | `a3f9c21` (branch `main`) |
| Catalog | application-assessment v3 · catalog 1.0.0 (`a2369a69e155`) — 153 items (137 applicable, 16 N/A) |
| Scope | Node.js API + Next.js + MongoDB; mobile app and LLM out of scope (N/A) |
| Previous run | first run |

## Summary

| Severity | Compliant | Partial | Non-compliant | N/A | Points earned / possible |
|---|---:|---:|---:|---:|---:|
| Critical | 20 | 9 | 14 | 5 | 73.5 / 129 |
| Important | 36 | 17 | 28 | 8 | 89 / 162 |
| Minor | 7 | 2 | 4 | 3 | 8 / 13 |
| **Total** | 63 | 28 | 46 | 16 | **170.5 / 304 = 56.1** |

Main risks: any logged-in customer can see other customers' orders by changing the
number in the URL; login does not limit attempts, which allows password guessing;
administrative accounts do not require a second factor.

## 1. Non-compliant items

### 1.1 Critical

#### SEC-3.02 · BOLA/IDOR — Critical · Non-compliant

- **Criterion:** every route that receives an object identifier confirms, on the server, that the authenticated user is entitled to it.
- **Situation found:** the order routes fetch the record by `id` only, without comparing it to the logged-in user.
- **Reason for the status:** the control does not exist and there is no negative test (ASSESSMENT §2 and §3).
- **Basis:** `confirmed`
- **Evidence:** `src/modules/orders/orders.controller.ts:58` — `orders.findById(req.params.id)` with no `userId` filter; search `rg "findById\(req.params" src/` → 6 hits, 5 without an ownership check.
- **Reproduction:** log in as test user A, create an order, log in as test user B and call `GET /orders/<A's order id>` → 200 with A's data.
- **Confidence:** `high` — the route and the repository method were read end to end.
- **Human validation:** `required` (Critical).
- **Affected components:** `GET /orders/:id`, `PATCH /orders/:id`, `GET /orders/:id/invoice` and 3 other routes.
- **Impact / risk:** an authenticated customer walks through sequential IDs and reads name, address and items of other people's orders (personal data leak, with LGPD impact).
- **Recommendation:** always fetch by `{ id, userId }` in the repository layer and answer 404 when nothing is found. Add a test where user A tries to read user B's order and gets 404.
- **Retest criterion:** a negative cross-access test exists and passes in CI for all listed routes.
- **Estimated effort:** S (≤ 1 day)
- **References:** SEC-3.02 · OWASP API Security Top 10 (API1 — BOLA)

## 5. Suggested backlog

| Priority | ID | Task title | Severity | Effort | Score gain |
|---:|---|---|---|---|---:|
| 1 | SEC-3.02 | Check order ownership on every `/orders` route | Critical | S | +1.0 |
| 2 | SEC-2.04 | Rate limit per account and per IP on login | Critical | S | +1.0 |
| 3 | SEC-2.08 | Single-use, expiring password-recovery token | Critical | S | +1.0 |
| 4 | SEC-2.05 | Offer MFA for administrative accounts | Critical | M | +1.0 |

*(…other sections omitted in this example)*
````

</details>

After the report, Claude offers to turn the backlog items into well-defined tasks with `/spec:refine` if the `spec` plugin is installed.

## What these plugins do not do

- **The health checks are not a pentest, an audit or a certification.** They read the repository and score it against a catalog, with evidence for each item. The security check prepares a project for a human pentest; it does not replace one.
- **The privacy check is not legal advice.** LGPD compliance depends on context that code does not show (contracts, processes, legal bases). Legal conclusions need a lawyer or the DPO.
- **A missing proof is not a confirmed flaw.** Each finding says whether the problem was `confirmed` in the code or whether `no evidence found` in the repository (the control may exist elsewhere). Critical findings need human confirmation before anyone acts on them.
- **No guarantee of security, performance or compliance.** A high score means the catalog items found evidence, not that the application has no problems.
- **Nothing is merged or deleted without your OK.** `/spec:approve` shows each action and waits for your confirmation; `/spec:build` pushes only the task branch and opens its pull request; `/spec:review` posts only the comments you pick. Text inside issues, pull requests or conversations never counts as permission.

## Trust and quality

**What each plugin can change:**

| Plugin | Reads | Writes | Outside your computer |
|---|---|---|---|
| `checkup` | The whole repository; may run lint, typecheck, unit tests and build locally | Only the reports in `docs/checkups/` (Markdown and JSON); never commits | Nothing |
| `spec` | Repository, issues, pull requests, the conversations you point to | Refinement documents in `docs/specs/`, code and commits on the task's branch | Issues, board moves, push of the task's branch, pull request, the review comments you pick; `approve` asks before commenting, merging and deleting branches |
| `polish` | The project's interface files and design system | The pages, screens and tokens it builds or redesigns | Nothing: it runs no commands and downloads nothing |

**How it is checked:**

- **Evals:** 40 cases, at least 3 per skill, cover triggering, the safety rules, dry runs and abuse cases such as instructions planted in a pull request ([how to run](docs/EVALS.md)).
- **CI on every pull request:** manifest validation, catalog counts and fingerprints, references and links, the score arithmetic of the example above, and a secret scan of the whole history.
- **Threat model:** assets, trust boundaries, twelve abuse cases and their known limits ([THREAT-MODEL.md](docs/THREAT-MODEL.md)).
- **Reproducible scenarios** on public fictitious fixtures ([CASE-STUDIES.md](docs/CASE-STUDIES.md)).

## Compatibility

Made for every Claude Code surface that supports plugins (terminal, desktop app, VS Code); so far the manifests are validated with Claude Code 2.1.63 and 2.1.114, and the desktop app and VS Code are not tested yet; running the evals needs 2.1.269 or later. The `spec` plugin needs Claude Code 2.1.110 or later and works best with the GitHub CLI (`gh`). Tested versions, systems and known limits: [COMPATIBILITY.md](docs/COMPATIBILITY.md).

## Before using the task skills

The `/spec:*` skills use your **GitHub task board** when the project has one, through the GitHub connection you already have (or the GitHub CLI, `gh`). If something asks for access, just approve it when Claude asks. No board? They record everything in your project's documentation and keep working. No GitHub, or no version control at all? They adapt (local commits, or a change log file).

## FAQ

**Do I need to know how to code?** Not to install it or to use task refinement and the health checks.

**Do the skills change my project without telling me?** The health checks never change anything. The others show what they will do and ask for confirmation on important decisions.

**Where does the work get recorded?** Always in your project's documentation folder (under `docs/specs/`), whether or not you have a task board. The only way to skip it is to tell Claude explicitly not to document.

**The skill didn't show up in the list.** Open a new conversation after installing or updating.

**I want to create or edit skills, or understand the folder structure.** See the [technical documentation](docs/TECHNICAL.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

**I found a security problem.** Report it privately as described in [SECURITY.md](SECURITY.md), never in a public issue. Changes between versions are in [CHANGELOG.md](CHANGELOG.md).

## Recommended tools

Optional tools that make the plugins work better. None of them is required.

| Tool | Helps with | Notes |
|---|---|---|
| **[GitHub CLI (`gh`)](https://cli.github.com)** | The `/spec:*` skills: reading and creating issues, moving cards on the board, opening and merging pull requests | Install it and sign in with `gh auth login`. To move board cards, also run `gh auth refresh -s project`. Without it, `spec` still works through its fallback modes. A GitHub connector (MCP) also works. |
| **Slack or Discord connector** | `/spec:from-thread`, which reads a conversation from a link | Without one, paste the conversation into a `.md` file and give Claude the file path. |
| **[Caveman](https://github.com/JuliusBrussee/caveman)** | Even shorter chat replies, to save tokens | The plugins already follow their own concise style, with no flattery or filler (adapted from Caveman), and write reports and tasks in full sentences. Caveman goes further and cuts grammar in the chat. Entirely optional and **not tested with these plugins**. According to its README, the skill alone (`npx skills add JuliusBrussee/caveman -g`) sends nothing, while its CLI sends usage statistics by default, so install only the skill if privacy matters to you. Its style favors very short answers: try it before relying on it, since the reports and tasks of `checkup` and `spec` follow fixed, detailed templates. |

## Privacy

- The plugins are just text files (instructions for Claude). Installing them **copies** those files to your computer and runs no code of its own.
- The skills run inside your Claude, with your account and your permissions.
- The `/spec:*` skills read and write on GitHub (and in your project folder) because that is their job, always with your account.

## Contributing and roadmap

Contributions are welcome: see [CONTRIBUTING.md](CONTRIBUTING.md). Next on the roadmap: recorded results for the case studies, a supply-chain health check, a test-plan skill and a threat-model health check. Progress is tracked in [the project's issues](https://github.com/CaioGiasson/cainitech-plugins/issues).

## License

[Apache-2.0](LICENSE). Free to use, copy and adapt, including commercially, keeping the license notice.

---

<div align="center">

**One team, one way of working. Everyone with their own Claude.**

<sub>
<a href="docs/TECHNICAL.md">Technical documentation</a> ·
<a href="https://github.com/CaioGiasson/cainitech-plugins/issues">Issues</a>
</sub>

</div>
