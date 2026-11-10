# Catalog changelog

Version history of the four criteria catalogs (`skills/*/references/checklist.md`). Every report records the catalog version and the fingerprint of its pillar, so a score change can be traced to a change in the code or to a change in the method.

## Rules

- Any change to an item (ID, title, severity or criterion text) changes the pillar's fingerprint. `scripts/validate.py` fails until a new entry is added at the top of this file with the new version and fingerprints.
- Versions follow Semantic Versioning: **major** when items are removed, IDs change or severities change (scores stop being comparable item by item); **minor** when items are added; **patch** when only the wording of a criterion changes without changing what it requires.
- Each entry lists every changed item by ID, with the old and new severity when it changed. Removed items are listed as deprecated, never dropped silently.
- The fingerprint is the first 12 hex digits of the SHA-256 of the pillar's item blocks (from each `#### ID` heading to the next heading), with trailing spaces removed. `scripts/validate.py --fingerprints` prints them.

## 1.0.0 — 2026-10-14

| Pillar | Items | Critical · Important · Minor | Fingerprint |
|---|---:|---|---|
| security | 153 | 48 · 89 · 16 | `a2369a69e155` |
| performance | 163 | 9 · 82 · 72 | `309e4f508ac3` |
| privacy | 126 | 37 · 66 · 23 | `25cd5673ef51` |
| ai-readiness | 70 | 6 · 30 · 34 | `332f8570446c` |

Initial version. Derived from the *Senior checklist for application assessment — v3* (October 2026), plus complementary AI-readiness items. External references cited by the items: OWASP ASVS 5.0, OWASP Top 10:2025, OWASP API Security Top 10, LGPD (Law 13.709/2018), ECA Digital, Marco Civil da Internet and ANPD resolutions as cited in each item.
