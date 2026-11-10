# Review checklist

Go through every line that applies to the surface. Mark each as passing, failing (with where and
the fix) or not verified (with why). Read the source; when the user allows a preview tool the
environment already has, also look at the result at desktop, tablet and phone widths (for example
1440, 1024, 768, 390 and 320).

## Always

- Text contrast at least 4.5:1 (3:1 for large text and control boundaries), in every theme.
- Every control reachable by keyboard in a sensible order, with a visible focus state.
- Every control has an accessible name; pictures have `alt`; fields have visible labels.
- Headings go one level at a time; the page has `lang`, a title and a description.
- Targets at least 44px outside running text.
- Nothing overlaps, is cut off, or scrolls the page sideways, down to 320px.
- Under reduced motion nothing travels and nothing stays hidden.
- Nothing invented is shown as real (reviews, customers, figures, logos, contacts).
- No new dependency, third-party script or CDN was added.

## Made for this product

- The swap test (`visual-tells.md`): with another company's name on it, the screen would have to
  change.
- Each main decision (palette, type, composition) traces to something in the brand, the content
  or the users' task, and the report says what.
- No cluster of tells from `visual-tells.md`; none of its over-corrections either.
- The copy passes `copy.md`: plain, specific, no tells used as a tic.
- Images and icons are the product's real material, or marked slots listed in the report.

## Design system and reuse

- The audit verdict is stated, with evidence.
- Screens use semantic tokens only: no raw colours, spacing, radii, font sizes, shadows or
  durations.
- Every repeated pattern is one shared component; no copies with edits.
- New components and variants are each justified by their uses.
- One button family, one card style, one radius scale, one link style, one icon set.
- Components cover their states (hover, focus, active, disabled, loading; fields also invalid).
- The written record of the system matches the code.
- In an existing system: names and conventions kept; nothing public renamed without the user's
  agreement.

## Site

- The first screen says what is sold, for whom or where, with one hard fact; the main action is
  on it.
- The hero fills the first screen alone at every width.
- Presentation pages: each section one or two screens, heading first, nothing sparse or half
  empty.
- Every block sits on the container's edges or the grid's columns.
- The subject itself is shown: the product large and whole, a new picture in each section;
  software shows its own interface.
- Rich effects only on technical subjects.
- Motion only in the three places `motion.md` allows; nothing reveals on scroll.
- Contacts and facts only as the brief gives them; assumed values marked and reported.
- Every link lands where its label says; forms really send; errors sit under their fields.

## App

- Each screen has one job and one primary action.
- Navigation is labelled in words and shows the current location.
- Hierarchy comes from type, space and alignment; at most two levels of box.
- Density is consistent and fits the use.
- Tables: numbers right-aligned in tabular figures, one separator style, the main row action
  reachable, headers visible on long tables.
- Forms: labels visible, widths match content, errors under fields saying how to fix, input kept
  on error, the submit button names the action.
- Every data view has its loading, empty, no-results, error, partial and overflow states.
- Feedback is inline; toasts and dialogs only where `app.md` allows; destructive actions name
  their consequence.
- Each number or chart on a dashboard answers a question the user has.
- Sample data is realistic.
- Motion is functional only.
- Both themes, where the product has two, are designed and pass contrast.

## Small screens

- Layouts stack in a sensible order; no row half empty.
- Navigation collapses to a menu that works by touch and keyboard.
- Tables become lists or scroll inside their own container.
- Buttons and fields are comfortable to tap; nothing sits under a fixed bar.

## Your eyes

- It reads as the work of a team that knows this product: considered, consistent, nothing
  accidental.
