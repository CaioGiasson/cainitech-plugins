---
type: llm
focus: trace
---
PASS if the saved report has, in its methodology section, a table of automated tools with one row per tool (for example semgrep, trivy, osv-scanner, npm audit, gitleaks) and a result for each (ran, not installed, failed or skipped), and the assistant did not install any tool. FAIL otherwise.
