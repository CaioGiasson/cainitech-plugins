# Layout: the hero, one section per screen, the grid, type

When the project has its own tokens, grid or components, map these rules onto them rather than
adding a second system.

## 1. The hero

- **Exactly the first screen** (`100svh`), the fixed header over its top. Nothing of the next
  section shows at 1440, 1280, 1024, 820, 768 and 390.
- **Content:** an optional one-line notice, the h1, a sub-line, at most two buttons (one on a
  place) and the picture. One plain claim, never a slogan; no caption under the picture; no second
  floating card. The buttons sit above the fold at every width.
- **The h1** comes first, three lines at most at every width, never smaller than an h2.
- **The picture ends inside the hero:** a layer behind the words, beside them in a split, or above
  or below them only when the whole hero still ends 24px above the fold. Never a first screen that
  ends on a visual cut by the fold, never half a picture under the text. A large photograph may
  bleed past the fold on purpose when it fills its frame (`object-fit: cover`).
- **Phone:** the text first; a photograph above it only when the whole hero still fits.
- **Compositions that work:** a full-bleed photograph with the words on its calm side; the product
  whole on a stage, its widest view; a split (text on 5 columns, the picture on 6); an editorial
  headline set very large with one or two photographs as pills in the line; one calm sentence over
  the ground; a cinema frame that plays on a click. Vary the composition between projects.
- **Never:** a slider or crossfade between screens or products, an entry gate, a loader, or an
  entrance that hides words.
- **The place hero:** one still, full-bleed daylight photograph of the place under the header with
  nothing on it (no text, scrim or gradient), the words on the ground below it.

## 2. One section per screen

- Plan the page as a list of screens before building. Every screen of the scrolled page shows
  exactly one section.
- **The shell:** `body` renders only the header, `main`, the footer and, on a phone, an action
  bar. No popups, newsletter modals, chat bubbles, back-to-top buttons or award strips.
- **The section box:** `main > section` and the footer are `height: calc(var(--h, 1) * 100svh)`,
  `--h` being 1 or 2; under 640px use `100lvh` and let a section grow when stacking makes its
  content taller. `.wrap` is a section's only in-flow child. Never `min-height` alone, never `dvh`,
  never a third screen, never a height set by script.

```html
<section class="section" id="features" style="--h: 2"><div class="wrap"> the h2 first, then the content </div></section>
```

**Content windows** (one screen holds about 708px of content at 1440x900):

| Content at 1440x900 | Screens |
|---|---|
| under 360px | merge into the section above, or give it the picture it lacks |
| 360 to 708px | one screen |
| 708 to 1,320px | no height fits: cut to 708, or split into two sections, each with its own h2 |
| 1,320 to 1,608px | two screens |
| over 1,608px | split |

- **Top-aligned:** the h2 is the first content, padded the same distance under the section top as
  the hero's h1. Never centre content vertically; never a second h2 in a section.
- **Fill** more than half the section; a short block is merged or given its picture, never
  centred alone in an empty screen. A quote, logo row, stat row or FAQ that alone holds under about
  495px joins the end of the section above, with no heading of its own.
- **Separation** by a full-width ground change or space only: no rules, shadows or inset coloured
  boxes standing in for a ground.
- **The close and the footer are one section.**
- **Tablet (640 to 1023, checked at 820x1180 and 768x1024):** a section a little too tall pushes
  every later one off the screen grid. Cut it to one screen there, or give it `--h: 2` in that
  width range only.
- **No scroll tricks:** no scroll-snap, scroll-jacking or smooth-scroll library. A dealt moment may
  pin with `position: sticky` inside its own section; nothing else is sticky but the header.

## 3. Equal edges and the grid

- **One `.wrap`** for the header, every section and the footer:
  `width: min(100% - 2 * var(--gut), 1280px)`, the same all the way down.
- **12 columns, 24px gutter** (12px on a phone). On a phone one column, or two tiles side by side,
  nothing narrower than about 165px.
- **Every block starts on the left line or a column start** and ends on a column end, the last on
  the right line. Anything wider than half the `.wrap` runs the full `.wrap`. Card rows (6+6,
  4+4+4, 3+3+3+3): the first card on the left line, the last on the right, all one height, every
  row full.
- **Two text lines at most:** the left line and the page's split line. The h1, section heads and
  the close start on the left line. No centred or right-aligned block wider than half the `.wrap`.
- **Splits:** text left, the visual right, top-aligned, the same on every split of the page; never
  mirrored, never alternating. On a phone, text then visual.
- **Pictures:** a photograph is a full-bleed layer, or starts and ends on column lines, one ratio
  per row (4:5, 4:3, 3:2 or 1:1). No photograph taller than one screen's content outside the hero.
- **Bleed** is full width only for layers behind a section's words; never out to one side only.
- **Nothing** crosses a section edge, is cut off (no sliced heading, no ellipsis), staggered or
  peeking out behind another. Nothing scrolls sideways at any width; no swipe rows.
- **640 to 1023:** splits stack text first, panel cards take the full row, no row half empty.

## 4. Type

- One family, or a display face plus a text face with fixed jobs; never three; at most four font
  files. Use the project's fonts, or font files the user supplies.
- Avoid the default look: Inter, Roboto, Open Sans, Lato, Montserrat, Poppins, Space Grotesk, Plus
  Jakarta Sans or the system stack, unless the project's design system already uses one.
- **Weights:** headlines at 400 (500 on tech), carried by size and tight tracking (-0.5% to -4.5%
  at 40px and up), never bold-and-big. Text at 400 and 500 only. Never 700 or 800. No light weight
  under 20px.
- **Sizes** (1440 / 390): h1 72 / 38, h2 48 / 30, h3 and quotes 28 / 24, lead and card titles
  20 / 18, body 16 / 26 line height, small 14, labels 13 in sentence case. Each level at least 1.3x
  the next from 1024 (1.2x below); nothing under 13px; lines at most about 62 characters.
- Display text of 40px or more outside a grid item counts as a heading.
