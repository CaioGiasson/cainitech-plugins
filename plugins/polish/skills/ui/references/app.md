# App screens

For screens people work in: dashboards, admin panels, lists and tables, forms, settings, editors.
The measure is how fast and how surely a user gets their task done, not how striking the screen
looks. Sizes and class names here are defaults; the project's design system wins.

## 1. Start from the task

Before any layout, write one line per screen: who is here, what they came to do, and which object
they act on (an order, a customer, a document). Then:

- **One job a screen,** and one primary action for it. Everything else is secondary or lives
  elsewhere.
- The most frequent task is the fastest path; rare and destructive actions sit further away.
- Use the product's own nouns and verbs, the same word for the same thing everywhere.

## 2. Structure

- **A stable shell:** navigation and a content area that stay in place between screens. A page
  header with the screen's title, its primary action and, where needed, filters.
- **No marketing patterns inside the app:** no hero, no decorative bands, no entrance animation.
- **Density fits the use.** Data-heavy tools that people use all day are compact (rows of about
  32 to 40px, body text 14px). Occasional or consumer tools are roomier (rows of 44 to 56px, body
  16px). Pick one and keep it across the app.
- **Hierarchy from type, space and alignment first.** A box only for a discrete object or a
  separate region; two levels of box at most.
- Left-aligned content on one grid; a readable maximum width for text and forms, full width for
  tables that need it.

## 3. Navigation

- Items labelled in words. An icon may accompany a label; an icon alone only for a few universal
  actions, with an accessible name and a tooltip.
- The current location is always visible. Breadcrumbs when the structure is more than two levels
  deep.
- Group items by the user's tasks, not by the system's internals. Only what this product has.

## 4. Tables and lists

- **A table** when users scan, compare or sort many items by the same attributes. **A list** for
  a few attributes read item by item. **Cards** only when each item is visual or self-contained.
- Text left-aligned, numbers right-aligned in tabular figures with the same precision, units in
  the header.
- One row separator style (a hairline or spacing), not borders plus stripes plus shadows.
- The row's main action is visible or the row itself opens; a menu holds the rest.
- Headers stay visible on long tables. Sorting and filtering where the task needs them, with the
  current state shown.
- Long values truncate with the full value available; columns keep a sensible minimum width.
- The normal state is plain text. Colour and badges mark the exceptions that need attention.
- Selection and bulk actions appear only when rows are selected.

## 5. Forms

- A visible label above each field; placeholder text never stands in for the label. Help text
  under the label when needed.
- Field width matches the expected value (a postcode is short, an address long). One column by
  default; related short fields may share a row.
- Group fields under plain headings; long forms split into sections or steps with progress shown.
- Mark the minority: if most fields are required, mark the optional ones.
- Validate when the user leaves a field or submits, not on every keystroke. The error sits under
  its field, says what is wrong and how to fix it, and the user's input is kept.
- The submit button names the action ("Save changes", "Create invoice") and shows progress while
  it runs. Whether changes are saved is always clear.
- The right control for the data: a switch for an immediate on or off, a checkbox for a choice
  submitted with the form, radios for a few exclusive options, a select for many.

## 6. States

Every view that shows data is designed in all of these, not only the full one:

| State | What to design |
|---|---|
| Loading | The layout stays stable; a skeleton that matches the real content for waits over about 300ms, nothing for shorter ones; never a full-page spinner for a partial load |
| Empty, first use | One sentence on what belongs here and the action that adds the first item |
| Empty, no results | What was searched or filtered, and a way to clear it |
| Error | What failed, in plain words, whether the user's data is safe, and how to retry |
| Partial | Some data present, some failed or still loading |
| Overflow | Very long names, very many items, very large numbers, missing optional values |
| Permission | What the user cannot see or do, and why, without dead ends |

Controls have their own: hover, focus, active, disabled (with the reason available), loading.

## 7. Feedback and interruption

- Feedback appears where the action happened: the button, the row, the field.
- A toast only for the result of something that finished out of sight. Never for an action whose
  result is already visible.
- Prefer undo to a confirmation dialog. Confirm only what cannot be undone, and name the
  consequence in the dialog and on its button ("Delete 3 invoices").
- A dialog is for a short, focused task that needs the page behind it. Never a dialog on a dialog;
  long or complex work gets its own page or a side panel.
- Update the screen at once when an action is very likely to succeed, and roll back clearly if it
  fails.

## 8. Dashboards and data

- Start from the questions the user opens the screen to answer, in order of importance. Each
  element answers one.
- A number needs context to mean anything: a comparison, a target or a trend, and where possible
  a path to act on it. A number with none of these is decoration.
- A chart only when the shape of the data matters (a trend, a distribution, a comparison across
  many items). Few values read better as text or a small table.
- Plain chart styling from tokens: labelled axes, direct labels over legends where possible,
  colour used to distinguish, never to decorate.
- Do not open with a row of metric cards by reflex. Often the most useful first element is the
  list of things that need the user's attention.

## 9. Realistic content

Design and demonstrate with data shaped like the real thing: uneven numbers, names of different
lengths, some missing values, some long text, dates in the product's locale. Tidy sample data
hides the problems real data will show.

## 10. Themes and small screens

- Light and dark themes come from the same semantic tokens (`design-system.md`); both are
  designed and checked for contrast.
- At phone width the navigation collapses into a menu, multi-column layouts stack, and a table
  either becomes a list of its key fields or scrolls inside its own container (the page itself
  never scrolls sideways). Targets are at least 44px.

## 11. Motion

Functional only: hover, press and focus states, and short transitions (under about 200ms) that
show where something came from or went. No entrance animations, no scroll effects, no looping
decoration (`motion.md`).
