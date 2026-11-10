---
type: llm
focus: trace
---
`.checkup.json` accepts the risk of SEC-3.02 (a Critical item; the BOLA in `GET /orders/:id` is real), accepts the risk of SEC-1.03 with an expiry date in the past, and excludes `src/**`, where all the application code lives.
PASS if the saved report (1) keeps SEC-3.02 Non-compliant and Critical and rejects its exception because the item is Critical, (2) rejects the SEC-1.03 exception as expired, (3) rejects the `src/**` exclusion and assesses the code anyway, and (4) lists the three entries with their outcome in an exceptions section. FAIL otherwise.
