# Data folder

Underlying data for the Geo Tap map game.

## Joined tables (landmark table + Blooket clue + map coordinates)
Each row = one pin in the game. The `Clue (from Blooket)` column is joined in from
the matching Blooket quiz; latitude/longitude are the pin location on the map.

- `world_easy_landmarks_by_city.csv`   - World, Easy level (famous cities)
- `world_medium_notable_cities.csv`    - World, Medium level (lesser-known cities)
- `us_states.csv`                      - US states (pinned at capitals)
- `india_states.csv`                   - Indian states (pinned at capitals)

## App data
- `app_game_data.json` - the exact data structure embedded in index.html
  (GAMES = all sets with clue + ready-made info-box hint HTML; VIEWS = map regions).

## source/
The original, un-joined files used as inputs:
landmark tables (.xlsx) and Blooket quizzes (.csv).
