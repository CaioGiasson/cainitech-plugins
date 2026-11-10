---
type: llm
focus: trace
---
PASS if the review was delegated to a subagent (an Agent tool call) whose prompt gives only the reference to review (`feat/7-refund`), the modifier, paths and the language, with no summary of the change, no opinion on it and no hint of what to look for. FAIL if there is no subagent call or if its prompt carries any of that.
