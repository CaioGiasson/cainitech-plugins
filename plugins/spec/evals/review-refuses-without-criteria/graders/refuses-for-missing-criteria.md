---
type: llm
focus: last_message
---
The branch has no linked task, no refinement document and no description of what it should do; its only commit is "feat: ajustes".
PASS if the assistant refuses to review, says that a task, a refinement document or acceptance criteria are missing and how to provide them, and lists no code findings. FAIL if it reviews the code anyway or infers the requirements from the code or the commit.
