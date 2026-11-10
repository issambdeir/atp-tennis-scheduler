# ATP Tennis Scheduler

A Python simulation that generates an optimal match schedule for an ATP tour event.

- Builds a realistic tournament draw (Grand Slam, ATP 1000, ATP 500, or ATP 250) using the
  actual seeding rules for each format — seeds are placed into the bracket following the
  same quarter/section logic used in real ATP draws.
- Schedules matches across the tournament's courts and days, assigning each match a date,
  time slot, and court.
- Factors in player preferences (preferred weather and time of day) when adjusting the
  schedule, and simulates weather conditions for each match.
- Includes a small set of real season/tournament data (Wimbledon, ATP Paris, ATP Doha,
  ATP Brisbane) to run the simulation against.

## Running it

```bash
python3 main.py
```

You'll be prompted to choose which tournament/season to simulate; the script then builds
the draw and prints out the generated schedule.

## Files

- `main.py` — draw generation, scheduling, and the CLI entry point
- `players.py` — player data and preference generation
- `seasons.py` — tournament/season data
