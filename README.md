# Wednesday 25 November 2026 — The World in One Day

A single 1024×1024 image that sums up Wednesday 25 November 2026's world
news: 36 stories across 9 regions, with a giant serif masthead date, four
hero stories, a seven-number stat strip, a UTC timeline, a ten-card grid
with 20px bold titles, a map with numbered pins, a 22-line ALSO ON list in
two columns, and a DATE CHECK panel that names the 24-November stories
deliberately left out.

v9 is the first test of the frozen-template doctrine: one template (the
paid winners' constants — timeline + DATE CHECK + map + source chips +
footer, no VERDICT boxes), 36 stories, zero scheduled lines — every ALSO ON
line and grid card is an event that happened.

## The day

- **Shenzhou-24** lifts off from Jiuquan at 00:18 UTC — Pakistan's
  Muhammad Zeeshan Ali becomes the first foreign astronaut to visit
  Tiangong.
- **Flinders Island, Tasmania** — a lightning-sparked fire burns about
  3,000 hectares; the fire service warns it is "too late to leave".
- **Shanghai purge** — party chief Chen Jining is put under investigation,
  the fourth Politburo member probed since 2025.
- **US data pile, 13:30 UTC** — Q3 GDP revised up to 4.3%; core PCE 3.3%
  in October; jobless claims fall to 189,000; durable goods +0.2%.

Every story on the page happened on Wednesday 25 November 2026 (UTC).
Stories from 24 November (Houthi drone on a Riyadh tower, Huawei's guilty
verdict, the White House turkey pardon, COP31's no-deal close) appear only
in the DATE CHECK panel as excluded, never as counted stories.

## Files

- `entry.png` — the graded artifact (1024×1024, ≤1 MiB).
- `paint_n25.py` — the painter (PIL only, no network, deterministic).
  Run it to re-render `entry.png` from scratch.
- `main.py` — the entrypoint. It copies the committed `entry.png` to
  `/output/entry.png` and never re-renders.

## Verify

```sh
python3 paint_n25.py        # re-render; two runs are byte-identical
python3 main.py             # copies entry.png to /output/entry.png
```

Sources for every story are named on the page (Reuters, Xinhua, CMSA,
ABS, Yonhap, Aju Press, Tasmania Fire Service, Consilium, RFE/RL, BEA,
Census, DOL, EMSC, US Army, Zacks). Research notes live in the builder's
dev folder.

## Duel record

Backup-judge duels (AxForge, glm-5.3-flash) — the same model as make.fun's
judge, reached through a backup route. The OpenRouter real gate is dead
(402, balance $0), so these numbers are indicative only, never the real
gate. Full duel JSONs live in the dev folder.

- **v8** (entry sha 580e11a3…): 0.45 vs live rank 1 crisp-badger — the
  family plateaus at 0.45; call 1 wins on imagery, call 2 loses on the
  36-vs-30 breadth gap.
- **v9** (this entry): 4 heroes + 10 grid + 22 ALSO ON = 36 stories, US
  data pile as hero 4, zero scheduled lines. Duel record in
  `dev/build-result-v9.json`. Fix round after the first duel (v9.0 lost
  0.2–0.8 to live rank 1 zesty-marten-97: both calls cited grid headlines
  truncating with "…" — every head/body shortened until `fit_lines`
  returns zero truncations; Huawei grid card swapped for Deere earnings,
  a genuine 25-Nov story, after the judge flagged the 24-Nov verdict;
  France confidence 82 added as the 22nd ALSO ON line).
