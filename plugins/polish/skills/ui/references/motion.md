# Motion

Every page moves in three places, and nothing else moves. Content is readable at rest, without
script and under reduced motion: motion only adds to a page that is already whole. Each motion in
the plan names its purpose in a few words; a motion with no purpose is cut.

## The three layers

1. **The hero's entrance,** once on load: the h1 rises line by line out of word masks (700ms a
   line, the lines 80ms apart), then the lead, the buttons and the facts fade up 12px (520ms each,
   60ms apart). The hero's picture is never hidden: a photograph settles from scale 1.05 to 1 over
   1.1s, a window or object from .98 over 900ms. About 1.1s in all, never again on scroll. Without
   script, under reduced motion and in print the hero stands as written; never a loader or a delay
   before reading.
2. **One dealt moment** in a section of its own (two on a long page of eight sections or more),
   big enough to remember. Outside tech it is photo- or type-led: photographs that change in place
   as the section scrolls, a photograph that develops once, a statement whose words light up with
   the scroll. It may pin only with `position: sticky` inside its own section, is scrubbed to the
   scrollbar (it runs back on the way up) and shows a finished state at both ends. Shader and WebGL
   moments stay on tech.
3. **The hover and press layer** on every link, button, linked card and linked photograph.

## Tokens

Hover in 150ms, hover out 120ms, press 90ms, a menu opening 200ms and closing 120ms, an indicator
travelling 240ms, a photograph zooming 600ms in and 400ms out, a card loop cycle 3.2s.

Curves: one UI ease-out, `cubic-bezier(.2, .8, .2, 1)`, for every UI step;
`cubic-bezier(.22, 1, .36, 1)` for an entrance settling; `cubic-bezier(.65, 0, .35, 1)` only for
travel; linear for loops. No bounce, no overshoot. Move transform, scale and opacity only (a hover
also changes colours); never animate width, height, top, left, margin or padding.

## The hover layer

Hover moves only for a fine pointer (`@media (hover: hover) and (pointer: fine)`); keyboard focus
shows the same state; every hover control also works by tap and keyboard. Nothing resizes or
pushes a neighbour; no rotate, skew, glow or shine sweep.

| Part | Motion |
|---|---|
| Button | the fill steps 14% toward the ink (an outline gains a faint fill and a stronger border) and the box steps up 1px; press sinks it to 1px below rest and scales .985 |
| Arrow | moves 3px right and settles back; one arrow style a page |
| Link | one underline style: a faint 1px hairline at rest, an ink line drawing left to right on hover |
| Nav | words take the drawn underline; a dropdown opens after about 150ms of intent with a 6px drop, one surface |
| Current page | a 2px bar under its nav word (`aria-current="page"`) |
| Card with a link | lifts 2px, its border darkens a step, an optional soft shadow (blur 24px, 10% ink at most) only on hover |
| Card without a link | nothing |
| Photograph in a link | scales 1.02 to 1.03 inside its frame (`overflow: hidden`); never dims or takes an overlay |
| Focus | a 2px ring in the action colour, 2px off the control, no transition |
| Field | the action-colour border and a 3px soft ring |

FAQs show every answer open: no accordion, nothing animates height.

## Tech only

- **Loops inside a card's visual:** one cycle of 2.5 to 4s, then it starts again; seeded on its
  finished picture, never an empty window; the pointer entering the card restarts it. One subject a
  cycle (a pointer clicks, a status turns, a bar fills, a line is written). One looping fragment
  per card group; a chart stays still.
- **One timed loop** a page, in the hero or the main visual, plus the one effect at most. Never two
  self-moving things in one screen.
- **A count** once a page, on load in the hero (about 1s), the final figure in the HTML.
- **A pause button** on anything still moving 5s after it is seen: a round 32px disc in the
  panel's bottom-right corner.
- Timed loops start on load and never start, stop or resume on scroll.

## Scroll

Outside the dealt moment's section (and a tech page's one big scene), nothing animates on scroll:
no card, row or tile reveal of any kind, no parallax or drift, no scroll-tinted ground, no progress
line, no count on view. The header looks the same at every scroll position.

## Reduced motion, no script, phones

Under `prefers-reduced-motion`, colours still change and menus fade, but nothing travels: a press
shows as a deeper tone, underlines appear without drawing, every loop, effect and moment shows its
finished frame, numbers show their final text, pause buttons hide. Nothing stays hidden. On a phone
card loops and effects hold their finished picture, there are no hover states, the hero still
enters and only light moments run (transform, clip-path, filter or colour; no WebGL).

## Never

- A card, row or tile that reveals, staggers, slides or fades in as the page scrolls; parallax on
  text; a scroll scrub outside the moment's section; a shader or WebGL moment outside tech.
- A heading that rises on every section, a second hero entrance, an entrance longer than about
  1.1s, or one that hides text a visitor could already be reading.
- A card that tilts, flips, scales, follows the pointer or glows at the cursor; a magnetic button.
- A carousel, an auto-advancing slider, timed tabs, a rotating notice, a logo marquee.
- Random blinking: twinkling dots, glitter, flicker, hue cycling, scrambled text.
- A hover slower than its token, an overshooting ease, a delay before a button reacts, an animated
  focus ring, a second underline style, an animated width, height or margin.
