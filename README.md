# Geo Tap

A self-contained, mobile-friendly geography game and a companion library of study
materials for Geography Bee prep. Tap the correct place on a map to answer
single-sentence clues, then download matching Blooket quizzes, landmark tables, and
printable map worksheets.

The game is a single HTML file with all of its data embedded — no build step, no
server. Open `index.html` in any browser (or host it on GitHub Pages) and play.

## Play it

Open `index.html` directly, or serve the folder locally:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

The only network calls the app makes are to the public Wikipedia/Wikimedia API to
fetch the photo and blurb shown in the info box. Everything else runs offline.

## Repository layout

```
.
├── index.html                  # The game — fully self-contained (GAMES + VIEWS data embedded)
├── data/                       # Data layer behind the game (has its own README)
│   ├── app_game_data.json      #   exact data structure embedded in index.html
│   ├── *.csv                   #   joined tables: one row per map pin (clue + lat/lng)
│   └── source/                 #   original un-joined inputs (landmark tables + Blooket quizzes)
├── materials/                  # Generated, ready-to-use study content
│   ├── blooket/                #   Blooket import quizzes (.csv + .xlsx)
│   ├── geography-bee/          #   Geography Bee tables (.xlsx)
│   ├── landmark-tables/        #   Landmark reference tables (.csv + .xlsx)
│   └── worksheets/             #   Printable map-labeling worksheets + study sheets (.pdf)
├── tools/
│   └── make_blooket.py         # Convert a Question/Answer CSV into a Blooket import CSV
├── docs/
│   └── making-geography-quizzes.md   # Recipe for building new study sets
├── skills/                     # Claude skill bundles used to generate the materials
│   ├── blooket-quiz.skill
│   └── map-worksheet.skill
└── tests/
    └── blooket-skill-test-review.html  # Eval review for the Blooket skill
```

## How the pieces fit together

1. **Source inputs** (`data/source/`) — landmark tables and Blooket quizzes per topic.
2. **Joined tables** (`data/*.csv`) — each source table joined with its Blooket clue and
   the pin's map coordinates; one row = one pin in the game.
3. **App data** (`data/app_game_data.json`) — the same structure embedded inside
   `index.html` as the `GAMES` (sets, clues, info-box HTML) and `VIEWS` (map regions) objects.
4. **Materials** (`materials/`) — distributable study content (quizzes, tables, worksheets)
   built from the same topics for offline practice.

See `data/README.md` for details on the data layer.

## Making new study sets

The fastest path is the copy-paste prompt in
[`docs/making-geography-quizzes.md`](docs/making-geography-quizzes.md), which produces a
landmarks table plus a matching Blooket quiz for any topic.

To turn a hand-written `Question,Answer` CSV into a Blooket-ready import file:

```bash
python3 tools/make_blooket.py questions.csv blooket.csv [time_limit]
```

The script builds three random distractors per question from the answer pool, marks the
correct choice, and writes Blooket's 8-column import format.

## Notes

- `data/source/` intentionally keeps its own copies of the source inputs so the data
  pipeline is self-contained; the same topics also appear as polished deliverables under
  `materials/`.
- The game data is embedded directly in `index.html`; if you regenerate
  `data/app_game_data.json`, re-embed it to update the game.
