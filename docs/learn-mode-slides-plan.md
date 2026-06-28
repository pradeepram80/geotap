# Plan: Interleave Google Slides into Learn mode

Status: **Not started — design agreed, awaiting input.** Captured 2026-06-25.

## Goal

Let a teacher run a single guided lesson in Geo Tap **Learn mode** that mixes their
own Google Slides with the existing map cards. The big panel that currently shows the
map should be able to show **either a map or a slide**, and the same **Next / Prev**
controls step through the whole mixed sequence — "slide, slide, map, slide, map…".

Requirements confirmed with the user:
- **Each single slide is its own Next-step** (not the whole deck in one card).
- The teacher can **specify the order**, freely interleaving slides and map content.
- The teacher **provides the deck only** (a file); Geo Tap converts it to images behind
  the scenes — the teacher never has to make images themselves.

## Chosen approach

**Slides shown as pre-rendered images** (not a live Google Slides embed). A live embed
was rejected because advancing it one slide per click from our own button is unreliable
(Google's embed wants to drive its own arrows). Images give perfect per-slide stepping,
work offline in a classroom, and are fully controlled by our Next/Prev.

Tradeoff accepted: if the teacher edits the deck later, they re-export and we re-convert.

## How it works

1. **Teacher provides the deck** as a file dropped in the repo — `deck.pdf` (preferred;
   from Google Slides: File -> Download -> PDF) or `deck.pptx`.
2. **Conversion (automatic, in the sandbox):** the deck is rendered to one PNG per slide
   into a `slides/` folder (e.g. `slides/slide-1.png`, `slides/slide-2.png`, …).
   - PDF: `pdftoppm -png -r 150 deck.pdf slides/slide`
   - PPTX: `libreoffice --headless --convert-to pdf deck.pptx` then `pdftoppm`.
   - Verified tooling available: LibreOffice 26.2, pdftoppm (poppler), ImageMagick
     `convert`, python-pptx, pdf2image.
3. **Lesson list (teacher-editable, ordered):** a clearly-commented array near the top of
   `index.html` defines the sequence. Each entry is a slide or a piece of map content:

   ```js
   LESSON = [
     { slide: 1 },                          // slides/slide-1.png
     { slide: 2 },
     { map: "India: Kerala" },              // a single place
     { slide: 3 },
     { map: "India" },                      // a whole set (steps through its places)
     { slide: 4 },
     { map: "World / Easy / Europe" },      // a region group
   ]
   ```

   Default if unspecified: **all slides first, then the maps.**
4. **Learn-mode UI change:** the Learn panel (`#lwrap` / `#lmap`) becomes able to show
   either the map SVG (place steps) or an `<img>` of a slide (slide steps). Next/Prev
   walk the combined LESSON sequence instead of only the map pins.

## What's still needed from the user

- The deck file in the repo (`C:\Dev\GeoTap\deck.pdf` or `.pptx`).
- The desired interleave order (or "default").

## Build checklist (when resumed)

- [ ] Convert provided deck to `slides/slide-N.png`.
- [ ] Add a `LESSON` config array (commented, editable) parsed into a unified step list.
- [ ] Extend Learn mode so a step can be a slide image or a map place/group.
- [ ] Make Next/Prev (and Autoplay) traverse the combined sequence.
- [ ] Show the slide image in the map panel, scaled to fit; keep the map for place steps.
- [ ] Sync to `C:\Dev\GeoTap`, verify, and commit.

## Notes / open questions

- Decide whether slide steps still show the info box / score chrome (probably hidden for
  slides — they are just teaching screens).
- Consider a simple way to map a `LESSON` "map" entry to existing `GAMES` data
  (set name, optional level/region, optional single place by `n`).
- Optional later: a "present"/kiosk full-screen mode and bigger text for projecting.
