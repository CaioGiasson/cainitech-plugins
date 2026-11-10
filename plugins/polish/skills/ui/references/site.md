# Sites and landing pages

For public pages that present and sell. A good company's site says plainly what is sold, shows the
real thing on every screen, and looks made for this client.

Sizes, class names and compositions here are defaults and examples. Where the project has a design
system, map these rules onto its tokens, grid and components instead of adding a second set.

Content-heavy pages (documentation, articles, catalogues, legal pages) follow the grid and type
rules but scroll naturally; the one-section-per-screen rhythm of section 4 is for presentation
pages.

## 1. The kind of business decides the page

Write the kind on the plan's first line.

| Brief | Kind |
|---|---|
| App, SaaS, AI, developer tool, fintech, a studio selling its own software | software |
| A game, a studio launching its game | gaming |
| Hardware or a technical device | tech |
| Any other physical product or brand | product |
| People are hired: clinic, law firm, agency, creative studio, trade | service |
| People come to it: cafe, bar, bakery, restaurant, guesthouse, shop, gym | place |

A maker that also opens its door or teaches is a **place**; its web shop becomes the goods
section.

"Technical" below means software, gaming or tech. Rich effects (shader grounds, WebGL scenes,
looping UI demos, counters, dark heroes) suit technical subjects. Every other kind is carried by
photographs, flat colour, type and real icons.

## 2. The page plan by kind

- **Place.** Photographs lead (a full page typically holds 12 to 20; a compact one 8 to 12). The
  hero is a real daylight photograph of the place. The visit block (address, hours, getting there)
  comes second, then the offer, the place itself, orders or booking. The offer and the place use
  different compositions, never two sections round one picture. One main action a screen.
- **Product and service.** Photographs lead: the product, the people, the rooms, the work. Flat
  grounds; one still diagram at most.
- **Every product page:** the product large and whole, filling most of its frame. A different
  picture in each section. Every promise in a headline is pictured. A colour swatch changes the
  picture. No fact stated twice.
- **Technical.** The client's own subject leads, at true size. Software shows its own interface
  as live HTML doing its real work (a code-review tool shows a diff with its accept action),
  never a generic dashboard. A game leads with its name and its world as key art. About 60 to 80
  words a screen outside interface mock-ups. One rich effect at most.
- **One object never carries the page.** The product leads the hero and at most two more
  sections; other kinds of visual carry the rest (in use, close-up parts, the people, a diagram,
  a large type moment).
- **The client's own assets get slots.** A trailer, screenshots or renders the brief names each
  get a frame that reads as finished, with a code comment naming the file the client will send.

## 3. The hero

- **Exactly the first screen,** with the header over its top. Nothing of the next section shows
  at common widths (1440, 1280, 1024, 820, 768, 390).
- **Content:** an optional one-line notice, the h1, a sub-line, at most two buttons (one on a
  place) and the picture. One plain claim, not a slogan. The buttons sit above the fold at every
  width.
- **The h1** comes first, three lines at most at every width.
- **The picture ends inside the hero:** a layer behind the words, beside them in a split, or
  above or below them only when the whole hero still fits. Never a first screen that ends on a
  visual sliced by the fold. A large photograph may bleed past it on purpose when it fills its
  frame.
- **Phone:** the text first.
- **Compositions to choose from,** by what the product has to show: a full-bleed photograph with
  the words on its calm side; the product whole on a stage; a split (text beside the picture); an
  editorial headline set very large; one calm sentence over the ground; a film frame that plays
  on a click. Choose from the material, say why in the plan, and vary between projects.
- **Avoid:** a slider or crossfade between products, an entry gate, a loader, an entrance that
  hides words.
- **A place's hero:** one still, full-bleed photograph of the place with nothing on it, the words
  on the ground below.

## 4. One section per screen

On presentation pages, plan the page as a list of screens: every screen of the scrolled page
shows one section, each one or two screens tall.

- **The shell:** the header, the main content, the footer and, on a phone, an optional action
  bar. No popups, newsletter modals, chat bubbles, back-to-top buttons or award strips.
- **The section box:** a height of one or two viewport units, set in CSS (for example
  `height: calc(var(--screens, 1) * 100svh)`), growing on small screens when stacking makes the
  content taller. One container inside it. Never a height set by script.
- **Content windows** (a screen holds roughly 700px of content at 1440x900):

| Content height at 1440x900 | Do |
|---|---|
| under about 360px | merge into the section above, or give it the picture it lacks |
| about 360 to 700px | one screen |
| about 700 to 1,300px | cut to one screen, or split into two sections |
| about 1,300 to 1,600px | two screens |
| more | split |

- **Top-aligned:** the h2 is the first content of its section. Do not centre content vertically.
- **Fill** more than half the section; a short block (a quote, a logo row, a few facts, a short
  FAQ) joins the section above instead of floating alone in an empty screen.
- **Separation** by a full-width ground change or space, not rules and shadows.
- **Tablet widths** (around 768 and 820): check that a section slightly too tall does not push
  every later one off the rhythm; cut it or give it two screens there.
- **No scroll tricks:** no scroll-snap, scroll-jacking or smooth-scroll library.

## 5. Equal edges and the grid

- **One container** for the header, every section and the footer, the same width all the way
  down (for example `width: min(100% - 2 * gutter, 1280px)`).
- **A 12-column grid** with one gutter. On a phone, one column, or two tiles side by side.
- **Every block starts on the left edge or a column start** and ends on a column end. Card rows
  are full, equal in height, and run from the left edge to the right.
- **Two text edges at most:** the left edge and one split line used on every split. Headings
  start on the left edge.
- **Splits** keep one orientation down the page (text one side, visual the other); on a phone,
  text then visual.
- **Pictures** are full-bleed layers or start and end on column lines, one ratio per row.
- **Nothing** crosses a section edge, is cut off, staggered or peeking from behind another.
  Nothing scrolls sideways.

## 6. Pictures

- Real photographs of the real thing wherever they fit; never stock passed off as the client's
  product, people or place. A stand-in is marked as one in the report.
- By default no caption under a picture; credits in one footer line.
- Every visual renders at every width; an effect that cannot run shows a still.

## 7. Type defaults for sites

These apply only when the project and the brand give no type system (`design-system.md`).

- Display sizes carry headlines: by default h1 around 72px at desktop and 38px on a phone, h2
  48 / 30, h3 28 / 24, lead 20 / 18, body 16 with generous line height, nothing under 13px.
- Headlines at regular or medium weight with tight tracking, carried by size, rather than
  bold-and-big.
- Lines of at most about 62 characters.
