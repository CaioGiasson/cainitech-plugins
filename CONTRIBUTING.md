# Contributing

## Setup

The plugins are Markdown instructions; there is nothing to build. You need [Claude Code](https://code.claude.com) and Python 3.10+ (for the validations).

Load the plugins from your working copy without installing them:

```bash
claude --plugin-dir ./plugins/checkup --plugin-dir ./plugins/spec --plugin-dir ./plugins/polish
```

The folder structure, the shared files and the rules for adding a skill or a plugin are in [docs/TECHNICAL.md](docs/TECHNICAL.md).

## Validations

Run before every pull request. CI runs the same checks:

```bash
claude plugin validate .
claude plugin validate plugins/checkup
claude plugin validate plugins/spec
claude plugin validate plugins/polish
python3 -X utf8 scripts/validate.py
```

`scripts/validate.py` checks the catalog counts, IDs, header totals and fingerprints against `CATALOG-CHANGELOG.md`, the `${CLAUDE_PLUGIN_ROOT}` references, the frontmatter of every `SKILL.md`, the shared `STYLE.md`, internal Markdown links, forbidden files and the arithmetic of the example report in both READMEs (points, score and classification). CI also scans the history for secrets with gitleaks.

## Evals

Every skill has at least three eval cases in `plugins/<plugin>/evals/` ([docs/EVALS.md](docs/EVALS.md)). A pull request that changes a skill's behavior adds or updates its cases. Run the suites of the changed plugins before every release; they need Claude Code 2.1.269+ and are billed to your account, so CI does not run them.

## Rules for changes

- **Catalogs:** any change to an item needs a new version in [plugins/checkup/references/CATALOG-CHANGELOG.md](plugins/checkup/references/CATALOG-CHANGELOG.md); `scripts/validate.py` fails otherwise. Scores between runs depend on them.
- **Side effects:** a skill never pushes, merges, deletes or publishes without the confirmation it documents. Content from issues, pull requests, conversations or code is data, never instructions (`plugins/spec/references/WORKFLOW.md` §7).
- **Style:** every skill reads `references/STYLE.md`. The file is identical in every plugin; change all copies together.
- **Versions:** bump the `version` of every plugin you changed, once per pull request, and add an entry to [CHANGELOG.md](CHANGELOG.md).
- **Bilingual docs:** `README.md` and `README.pt-BR.md`, `docs/TECHNICAL.md` and `docs/TECNICO.md` change together.
- **No secrets or personal data** in skills, examples, issues or pull requests.

## Proposing a skill

Open an issue first with the problem it solves, who uses it, its side effects and how it overlaps with existing skills.

## Reporting bugs and unsafe behavior

- Bugs and wrong results: open an issue with the plugin, skill, version, steps and the smallest example.
- Unsafe behavior or vulnerabilities: follow [SECURITY.md](SECURITY.md), never a public issue.
