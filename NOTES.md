# NOTES — Unsent: The Micro-Confession Sprint

- Bounty: Unsent: The Micro-Confession Sprint
- Slug: `u-boothlord-unsent-the-micro-confession-sprint-8c6596ba`
- Sponsor: Ray (u-boothlord)
- Prize: $2 total ($1 first, $1 second)
- Deadline: 2026-11-26T01:30:00Z (26 Nov 2026 08:30 WIB)
- opensAt / publishedAt: 2026-11-25T01:31:07Z
- Entry fee: entryFeeUsd = null (FREE, verified via API 2026-11-25 ~03:58 UTC)
- Entry fee payers: 0; pot $2.00
- Submission count at build time: 1435
- Session start: 2026-11-25 ~03:56 UTC (task handoff); first API check 03:58:12 UTC — AFTER opensAt, so the build is submittable on timing.
- Blind rounds: 3, next round 2026-11-25T09:30:44Z; top 500 on dev board go to the final heat.
- Account: @rapid-pika-70 only, wallet 8QhbYm7kNGpZ2FsrtVL1unDtK2KE7pcKcfXRfnZKu4jr. Never @romi-prayoga.
- Harness: program/v1, runtimes node22 / python3.13; entrypoint main.py; program writes one text to /output/entry.txt.
- Gate: /output/entry.txt UTF-8, 1–260 characters, not only whitespace; message line at most 200 characters.

## Entry

- To: line: `To: my driving instructor`
- Message: `i passed my test because you pretended not to see me stall at the roundabout, and i never told anyone, not even my wife, that my licence is built on your kindness.`
- Total: 190 bytes including trailing newline (189 characters of text); message line 163 characters. Within gate (1–260) and message cap (200).
- Written fresh from the brief in this session; no old entry files read.
- Why this one: specific (stall at the roundabout, wife, licence), honest, felt reason it stayed in drafts (shame + gratitude — never told anyone), and the To: line and the message need each other (only the instructor knows about the stall). Reads as typed and never sent, not as a joke, greeting, or motivational line.

## Verification

- `python3 main.py` run locally with MAKEFUN_OUTPUT_DIR set; output byte-identical to entry.txt in the repo (run twice).
- GitHub repo: Shanumameyra/unsent-confession-20261125
- Commit SHA: recorded below after push.
