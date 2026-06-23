# How to Make a New Geography Study Set (Table + Blooket Quiz)

This is a reusable recipe for building a landmarks **table** and a matching **Blooket quiz**
on any geography topic — countries of a continent, rivers of the world, national parks,
world capitals, mountain ranges, and so on.

The easiest method is to **paste the prompt below to Claude** and just change the topic in
the first line. Claude does the research and the Blooket formatting; you get two Google Sheets.

---

## ✅ The Copy-Paste Prompt

> Create a geography study set for the topic: **<PUT YOUR TOPIC HERE>**
> (for example: "countries of Africa", "major rivers of the world", "US National Parks",
> "European capitals", "mountain ranges of the world").
>
> Audience: 5th-grade level, for my 8-year-old preparing for a Geography Bee. Keep all
> facts accurate, and double-check anything that may have changed recently (capitals,
> records, "newest/largest", etc.).
>
> **1) TABLE** — one row per item, with these columns (adjust or drop any that don't fit
> the topic, and add ones that do):
> *Item · Capital/Location · Natural Landmarks · Man-Made Landmarks · Nickname ·
> Major Trade/Industry · Cultural Aspects · Interesting Facts*
>
> **2) BLOOKET QUIZ** — one question per item. Each question must be **one single sentence**
> that starts with a *harder, lesser-known clue* and ends with an *easy, well-known clue*,
> in exactly this style:
> *"Arctic foxes are found in Svalbard, an archipelago belonging to which Scandinavian
> country also known as the land of the midnight sun?"*
> The **answer is the item's name** (the state/country/river/etc.). Give 4 answer choices
> (1 correct + 3 distractors of the same type) and mark the correct one, using Blooket's
> 8-column import format: *Question #, Question Text, Answer 1, Answer 2, Answer 3,
> Answer 4, Time Limit (sec), Correct Answer(s)*.
>
> **3) OUTPUT** — make both as **Google Sheets** in my Drive (one for the table, one for the
> Blooket quiz) and also save .csv and .xlsx copies in my Geo Bee Prep folder.

That's it. You can tweak any line — for example:
- **Number of items:** "just the 15 most important", or "every one".
- **Answer type:** "the answer should be the capital city" instead of the country.
- **Difficulty:** "make the clues a little harder" or "shorter".
- **Distractors:** "make the wrong answers regionally similar so it's harder."

---

## 📥 Loading the quiz into Blooket

1. Go to the Blooket Set Creator and choose **CSV Import**.
2. Give the set a title and click **Create Your Set**.
3. Upload the Blooket CSV (or open the Google Sheet, then **File → Download → CSV** first).
4. Blooket fills in all the questions — review and play.

The 8 columns Claude produces already match Blooket's template, so it imports directly.

---

## 🛠️ Optional: Do-It-Yourself Converter

If you ever want to **write the questions yourself** and just need them turned into the
Blooket format (with random wrong answers and the correct-answer number filled in), use the
included script **`make_blooket.py`**.

1. Make a simple CSV called `questions.csv` with two columns: **Question** and **Answer**.
   Example:

   | Question | Answer |
   |---|---|
   | Old Faithful erupts in Yellowstone, in which least-populated US state, also the first to let women vote? | Wyoming |
   | The Golden Temple at Amritsar stands in which state, also called the Land of Five Rivers? | Punjab |

2. Run it (Claude can do this for you):
   `python3 make_blooket.py questions.csv blooket.csv`

3. The script reads your questions, builds 3 random wrong answers for each from your list of
   correct answers, marks the right one, and writes a Blooket-ready CSV.

The clever part — writing the single-sentence "hard clue → easy clue" questions — is still
best done by Claude. The script only handles the mechanical formatting.
