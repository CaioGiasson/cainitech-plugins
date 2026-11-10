# Security policy

## Supported versions

Only the latest version of each plugin (`checkup`, `spec`, `polish`) receives fixes. Update with `claude plugin marketplace update cainitech` followed by `claude plugin update <plugin>@cainitech`.

## What to report

- A skill that takes an action with side effects (push, merge, branch deletion, comment, board move, message) without the confirmation it documents.
- A skill that follows instructions found in repository content, issues, pull requests or conversations instead of treating them as data.
- A skill that writes secrets or personal data into reports, issues, pull requests or docs.
- A skill that runs commands, downloads files or sends data to destinations it does not document.
- A vulnerability in the CI of this repository.

Wrong scores or findings of a health check are quality bugs, not vulnerabilities: open a regular issue.

## How to report

Report privately through GitHub: open the **Security** tab of this repository and choose **Report a vulnerability**. Do not open a public issue for a vulnerability.

Include:

- the plugin, the skill and its version (`claude plugin list`);
- the Claude Code version and the surface (CLI, desktop, VS Code);
- the steps to reproduce, with the smallest example that shows the problem;
- what happened and what you expected.

**Never send real secrets, tokens, passwords or personal data.** Replace them with fake values in examples and logs.

## What to expect

- Acknowledgement within 7 days.
- An assessment and a plan within 30 days.
- Credit in the release notes, if you want it.

The assets, trust boundaries and known limitations are documented in the [threat model](docs/THREAT-MODEL.md).

These plugins are text instructions run by Claude with your own account and permissions. They are not a security product and come with no warranty (see [LICENSE](LICENSE)).
