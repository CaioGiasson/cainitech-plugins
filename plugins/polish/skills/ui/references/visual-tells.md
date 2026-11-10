# Visual tells of AI-made interfaces

What makes an interface read as generated, and the fix for each. One tell proves little; clusters
are the signal. The tells move with every model generation, so learn why each one reads as a
default instead of memorising the list.

## Why it happens, and the test

A model picks, at each decision, the option that fits the most products. Each choice is
reasonable; together they are the template everyone has seen. And because each screen is styled
from scratch, small differences pile up between screens.

**The swap test.** Replace the logo and the product name with a different company's. If nothing
else on the screen would have to change, the screen says nothing about this product. Find what the
product really has (its subject, its content, its data, its users' task, its brand) and let that
drive the composition.

**A tell is a default, not a ban.** Everything below is fine when the product's brand or content
calls for it (a brand that is purple, a product that really has three plans). It is a tell when it
is there because nothing else was decided.

## Colour

| Tell | Fix |
|---|---|
| Violet or indigo as the accent, a purple-to-blue gradient as the "brand" | The palette comes from the brand; with none, from the product's subject, with the reason stated |
| Gradient text on headings; a gradient on every button and band | Flat colour from tokens; a gradient only where the brand owns one |
| Coloured glow shadows; neon accents on near-black as "dark mode" | A dark theme designed as a scale of surfaces, the same roles as the light one |
| A different pastel tint on each card or icon | One action colour; other colours only carry meaning |
| Green, red and amber badges as decoration | State colours only for states |
| Pale grey text on a grey ground | Contrast checked for every text and ground pair |

## Surface and decoration

| Tell | Fix |
|---|---|
| Everything is a card: rounded corners, soft shadow and a hairline border at once | Group with space and type first; a card only for a discrete object; one separator, not three |
| Cards inside cards inside cards | Two levels of box at most |
| Frosted glass and background blur on panels | Opaque surfaces from tokens |
| Blobs, mesh gradients, floating orbs, dot or grid patterns behind content | The product's own material (its UI, its photographs, its data) or a plain ground |
| The same large radius and the same shadow on every element | One radius scale and two or three elevation levels, each with a job |

## Layout

| Tell | Fix |
|---|---|
| Everything centred: heading, text, buttons, sections | Left-aligned on shared edges; centring kept for short, deliberate moments |
| The stock hero: a pill badge over a centred heading, two buttons, a screenshot below | A composition built from what this product has to show (`site.md`) |
| Three equal cards, each an icon in a tinted circle, a title and two lines | As many items as there are; show the thing itself; vary the form with the content |
| The same section skeleton all the way down: small label, heading, lede, card grid | Each section shaped by its content |
| The canonical page order: logo cloud, feature cards, zigzag rows, stat strip, three testimonials, three plans with the middle one flagged, FAQ accordion, gradient call-to-action band | Only the sections this product has real content for, in the order a visitor's questions come |
| A "bento" grid of unequal tiles holding unrelated things | A grid whose structure mirrors the content's structure |
| The same gap between everything | Space shows grouping: related things closer, sections clearly apart |
| Several left edges and widths down one page | One container and one grid for every screen |

## Type

| Tell | Fix |
|---|---|
| The framework's default font at default sizes | The brand's type, or a pairing chosen for the product, in a real scale |
| Hierarchy by bold and size alone; every heading the same weight | Hierarchy from scale, weight, colour and space together, each used sparingly |
| A tracked, uppercase mini-label over every heading | A label only where it adds information |
| Title Case On Every Heading And Button | Sentence case, unless the brand's style says otherwise |
| Centred paragraphs; lines running the full width | Left-aligned text, lines of about 45 to 75 characters |
| Emoji in headings, buttons and lists | Words; an icon from the project's set where one helps |

## Icons and images

| Tell | Fix |
|---|---|
| Emoji as icons; sparkles for anything "AI"; a rocket for launch | One icon set, one stroke weight, and only where the icon is understood |
| A decorative icon on every card and list item | An icon only where it speeds recognition |
| Icons mixed from several sets | The set the project already has |
| Drawn look-alikes of real logos; invented customer logos | Real files supplied by the user, or none |
| Generic illustrations, 3D shapes, mood stock, AI-looking pictures | The product itself: real UI, real photographs, real data; else a marked slot |
| A fake browser window holding a dashboard of meaningless charts | The product's actual screen, showing real work |
| Initials in gradient circles as a row of "users" | Real people with permission, or nothing |

## Motion

| Tell | Fix |
|---|---|
| Everything fades and rises in as the page scrolls | Content is simply there; motion follows `motion.md` |
| Cards that grow, tilt or glow on hover | Small, quick state changes on things that are interactive |
| Animated gradient borders, typewriter headings, bobbing elements, confetti | Motion that shows a state, a step or real data, or none |

## App screens

| Tell | Fix |
|---|---|
| A dashboard that opens with four KPI cards (number, arrow, percentage, sparkline) whatever the product | Start from the questions the user opens the screen to answer (`app.md`) |
| Charts as decoration; a doughnut for two values | A chart only when the shape of the data matters; often a sentence or a table |
| A grid of cards where the user needs to scan and compare | A table or a dense list |
| A coloured pill on every row | Plain text for the normal state; colour for the exceptions |
| Only the happy state designed: full, tidy data, no loading, empty or error | Every state designed (`app.md`, States) |
| Perfect sample data: round figures, short names, the same stock names and companies | Realistic data: uneven numbers, long names, missing values |
| An empty state with a big illustration and a cheerful line | One sentence on what belongs here and the action that adds the first item |
| A modal for everything; a toast after every click; a full-page spinner | Inline editing and inline feedback first (`app.md`, Feedback) |
| Several primary buttons on one screen; a gradient primary | One primary action a screen, in the action colour |
| Placeholder text used as the label; every field the same width | Visible labels; field width matched to the expected value |
| A sidebar with an icon per item, an upgrade card and decorations by reflex | Navigation that lists what this product has, labelled in words |
| Sparkle buttons and an assistant bubble added to look current | AI features only where the product has them, presented as plainly as any other |

## In the code

These are why screens drift apart, and they are fixed in the design system
(`design-system.md`):

- arbitrary one-off values, inline styles and raw hex colours scattered through screens;
- the same button or card restyled in several places;
- copies of a component with small edits;
- a new utility or wrapper per screen for what a shared component already does.

## Over-correction

Avoiding one default by reflex produces the next one.

| Rule applied | The new default it breeds | Counter |
|---|---|---|
| No purple | Teal or emerald on every product | Derive the palette from the brand or the subject |
| No stock SaaS look | Cream ground, a serif display face and a terracotta accent on everything | The same: decide from the product |
| Not the default font | The same replacement font every time | A pairing chosen per product, varied between projects |
| No cards | Walls of unstructured text | Group with space, type and alignment |
| Nothing centred | Every section the same left-right split | Composition follows content |
| Fewer colours | A grey interface with no clear action | One confident action colour |
| Be distinctive | Decoration and novelty that get in the way | Distinct through the product's own material, not ornament |

**Not tells:** a conventional layout that fits the content; a familiar navigation pattern;
standard controls; restraint. Users rely on convention. The aim is a considered interface, not an
unusual one.
