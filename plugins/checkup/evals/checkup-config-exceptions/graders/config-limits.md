---
type: llm
focus: trace
---
`.checkup.json` accepts the risk of SEC-3.02 (a Critical item; the BOLA in `GET /orders/:id` is real), accepts the risk of SEC-1.03 with an expiry date in the past, declares SEC-2.01 (an unconditional item) not applicable, and excludes `src/**`, where all the application code lives.
PASS if the saved report (1) keeps SEC-3.02 Non-compliant and Critical and rejects its exception because the item is Critical, (2) rejects the SEC-1.03 exception as expired, (3) rejects the SEC-2.01 exception because the item is not conditional and assesses it, (4) rejects the `src/**` exclusion and assesses the code anyway, and (5) lists the four entries with their outcome in an exceptions section. FAIL otherwise.
