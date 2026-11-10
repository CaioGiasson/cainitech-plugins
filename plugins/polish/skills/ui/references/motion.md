# Motion

Content is readable at rest, without script and under reduced motion: motion only adds to an
interface that is already whole. Every motion has a purpose that fits in a few words ("the link
answers", "the panel came from this button"); one without a purpose is cut.

Durations and curves below are defaults; define them as tokens in the design system and use the
project's own where they exist.

## Tokens

Hover in 150ms, hover out 120ms, press 90ms, a menu or panel opening 200ms and closing 120ms, an
indicator travelling 240ms, a picture zooming 600ms in and 400ms out.

Curves: one ease-out for interface steps (for example `cubic-bezier(.2, .8, .2, 1)`); a softer
one for an entrance settling (`cubic-bezier(.22, 1, .36, 1)`); an in-out curve only for travel;
linear for loops. No bounce, no overshoot. Move transform, scale and opacity (a hover also changes
colours); do not animate width, height, top, left, margin or padding.

## The interaction layer (sites and apps)

Hover moves only for a fine pointer (`@media (hover: hover) and (pointer: fine)`); keyboard focus
shows the same state; everything that reacts to hover also works by tap and keyboard. Nothing
resizes or pushes a neighbour.

| Part | Default motion |
|---|---|
| Button | the fill steps toward the text colour on hover; a press shows as a slightly deeper tone or a 1px sink |
| Link | one underline style across the product; the colour or underline changes on hover |
| Interactive card or row | a small change that marks it as clickable: the border or ground steps one tone, or it lifts 1 to 2px |
| Non-interactive card | nothing |
| Picture inside a link (sites) | scales 1.02 to 1.03 inside its frame |
| Focus | a 2px ring in the focus colour, offset from the control, with no transition |
| Field | the border takes the action colour, with a soft ring |
| Menu, popover, panel | fades in with a short move from where it was opened; closes faster than it opens |

## Apps

Functional motion only: the interaction layer above, plus short transitions (under about 200ms)
that keep the user oriented: a panel sliding from its edge, a row leaving a list, a value
updating in place. No entrance animations, no scroll effects, no looping decoration. A progress
indicator for anything that takes more than about a second.

## Sites

A presentation page may move in three places, and nothing else moves:

1. **The hero's entrance,** once on load: the words arrive in order, the picture settles. About a
   second in all, never again on scroll. The picture is never hidden; without script or under
   reduced motion the hero simply stands. Never a loader or a delay before reading.
2. **One chosen moment** in a section of its own (two on a long page), big enough to remember and
   chosen for the content: photographs that change in place as the section scrolls, a picture that
   develops once, a statement whose words light up with the scroll. It may pin with
   `position: sticky` inside its own section, follows the scrollbar in both directions and shows a
   finished state at both ends. Shader and WebGL moments suit technical subjects only.
3. **The interaction layer** above.

Outside that one moment, nothing animates because the page scrolled: no reveal of cards, rows or
sections, no parallax, no progress line, no count on view.

On technical pages only: a looping demonstration inside a visual (a cycle of 2.5 to 4 seconds,
starting on its finished picture, one loop on screen at a time) and one counter on load. Anything
still moving five seconds after it is seen gets a pause control.

## Reduced motion, no script, phones

Under `prefers-reduced-motion`, colours still change and menus fade, but nothing travels: loops,
effects and moments show their finished frame, numbers show their final value. Nothing stays
hidden. On a phone there are no hover states, heavy effects become stills, and only light motion
runs.

## Avoid

- Cards, rows or sections that fade, slide or stagger in on scroll; parallax on text.
- A heading that animates in every section; an entrance longer than about a second, or one that
  hides text a visitor could already be reading.
- Cards that tilt, flip, grow, follow the pointer or glow at the cursor; magnetic buttons.
- Carousels and sliders that advance by themselves, timed tabs, rotating notices, logo marquees.
- Random blinking: twinkling dots, glitter, hue cycling, scrambled or typewriter text.
- A delay before a control reacts, an overshooting ease, an animated focus ring.
