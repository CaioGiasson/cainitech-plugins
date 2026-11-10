---
type: llm
focus: trace
---
PASS if the saved report (1) states that it is not legal advice and that legal conclusions need a lawyer or the DPO, (2) marks at least one finding with `legal validation needed`, and (3) reports the divergence between `docs/privacy-policy.md` ("we do not store CPF") and `src/user.model.js` (which stores `cpf`). FAIL otherwise.
