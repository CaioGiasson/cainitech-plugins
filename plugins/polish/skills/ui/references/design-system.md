# Design system: audit, create, improve, reuse

A design system here means two things kept in the project's own code: **tokens** (named values for
colour, type, space, radius, elevation, motion) and **components** (shared building blocks with
variants and states). Its purpose is reuse: a decision is made once and every screen inherits it.

Work in the project's stack and conventions. Plain CSS gets custom properties; a Tailwind project
gets its theme configuration; a CSS-in-JS project gets its theme object; a component framework
gets components in its own idiom. Add no library to do this.

## 1. Audit

Read, do not guess. Look for:

- **Tokens:** CSS custom properties (`:root`, theme files), a Tailwind or UnoCSS theme, Sass
  variables, a theme object, a tokens file (JSON or similar).
- **Components:** a components or ui folder, a component library the project depends on, a
  Storybook or a docs page, existing design documentation (`DESIGN.md`, a style guide).
- **Brand material:** logo files, brand colours, fonts loaded, an existing public site.

Then measure drift in the screens:

- raw values used where a token exists or should (hex colours, pixel sizes, arbitrary utility
  values, inline styles);
- near-duplicate values (five greys two points apart, three radii one pixel apart);
- the same pattern built more than once (several button styles, several card looks, copies of a
  component with a suffix such as `2`, `New` or `Alt`);
- components missing states (no focus, disabled, loading, error or empty);
- tokens or components nothing uses.

**Verdict:**

| Verdict | Signs |
|---|---|
| **Healthy** | Tokens and shared components exist and screens use them; drift is small |
| **Partial** | Some tokens or components exist, but screens mix them with raw values and duplicates |
| **None** | Styles live in each screen; no shared tokens or components |

Report the verdict with counts as evidence ("14 distinct greys, 4 button implementations").

## 2. Create (verdict: none)

Build the smallest system the screens in scope need. Do not build a catalogue of components
nobody asked for.

### Tokens, in two tiers

1. **Primitives:** the raw scales (a neutral ramp, the brand hues, the spacing steps).
2. **Semantic tokens:** roles that point at primitives. Components and screens use **only**
   these. Typical roles: `bg`, `surface`, `surface-raised`, `text`, `text-muted`, `border`,
   `border-strong`, `action`, `action-hover`, `on-action`, `focus`, `danger`, `success`,
   `warning`, `info`. Name them in the style the codebase already uses.

A light and a dark theme are the same semantic names pointing at different primitives. When the
product has both, design both; neither is an inversion of the other.

### Where each scale comes from

- **Colour.** Start from the brand's colours. With no brand, derive the palette from the product's
  subject and audience and say why in the plan. One action colour. Neutrals tinted slightly toward
  the brand hue instead of pure grey. State colours (danger, success, warning) kept for states,
  never decoration. Check every text and background pair for contrast before using it.
- **Type.** The brand's fonts, or the fonts the project already loads, or files the user supplies.
  One family, or one display and one text family with fixed jobs. A scale with clear steps (each
  level at least 1.2x the next). Typical bases: a site reads at 16 to 18px with large display
  sizes; an app reads at 14 to 16px with a tighter scale. Two or three weights, each with a job.
  Tabular figures for numbers in tables.
- **Space.** One scale on a 4px base (for example 4, 8, 12, 16, 24, 32, 48, 64, 96). Space shows
  grouping: things that belong together sit closer than things that do not.
- **Radius.** One short scale and one personality (sharp, soft or round), chosen for the product.
  A nested corner is the outer radius minus the padding between them.
- **Elevation.** Two or three levels. Separate a surface by a border, a ground change or a
  shadow: one of them, not all three.
- **Motion.** The durations and curves of `motion.md` as tokens.
- **Breakpoints and layers.** A few named breakpoints and one z-index scale.

### Components

Start from the screens in scope and list what they repeat. The usual core, built only as needed:
button, link, field (label, help, error) with its inputs, select, checkbox, radio, switch, card or
surface, layout primitives (stack, cluster, grid, container), navigation, dialog, table, badge,
alert, empty state, skeleton.

Every component:

- uses semantic tokens only;
- exposes differences as a few consistent variant props (for example `variant`, `tone`, `size`),
  named the same way across components;
- covers its states: hover, focus-visible, active, disabled, loading, and for fields invalid and
  read-only;
- takes content of any length without breaking (long labels, no icon, many items).

### Write it down

Record the system where the project keeps its docs (ask if unclear; default `DESIGN.md` at the
project root): the tokens and their roles, each component with its variants and when to use it,
and the reuse rules of section 4. Keep it short and current. If the project has an agent context
file (`AGENTS.md`, `CLAUDE.md`), suggest adding one line pointing to it so later work reuses the
system; add it only with the user's agreement.

## 3. Improve (verdict: partial, or healthy with gaps)

The system belongs to the project. Improve it; do not replace it, and do not restyle the brand.

- Keep its names, file layout and conventions. No renames of public tokens or component props
  without asking.
- **Consolidate values:** merge near-duplicates into the nearest existing token; add a token only
  for a value that is really distinct.
- **Replace raw values** in screens with tokens.
- **Merge duplicate components** into one with variants; migrate the uses; remove the copies.
- **Fill missing states** and fix contrast failures.
- **Add the semantic tier** if only primitives exist and screens depend on them directly.
- Remove what nothing uses, after confirming with a search.

Propose the changes as a list ordered by reuse gain (how many screens each fixes), smallest safe
step first. Apply them incrementally so the product keeps working at every step; when a change is
wide, do the system first and migrate screens after.

## 4. Reuse rules (every job)

- Search for an existing component before writing UI. Say in the plan what is reused.
- A pattern that appears twice becomes a component. A true one-off stays local and still uses
  tokens.
- One dimension of difference is a variant. A structural difference is composition of existing
  parts. A copy with edits is never the answer.
- No raw colour, spacing, radius, font-size, shadow or duration in a screen. Missing value: add
  the token, then use it.
- Keep variant counts small. Before adding one, check that an existing one cannot serve.
- A new component earns its place by more than one use, or one use plus a clear next one named in
  the plan.
- Update the written record in the same change that touches the system.
