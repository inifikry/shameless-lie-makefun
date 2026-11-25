[![make.fun](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6.svg)](https://make.fun/c/u-danu-the-most-shameless-lie-fbb85bc6)
[![rank](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6/inifikry/shameless-lie-makefun/rank.svg)](https://make.fun/c/u-danu-the-most-shameless-lie-fbb85bc6)
[![reward](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6/inifikry/shameless-lie-makefun/reward.svg)](https://make.fun/c/u-danu-the-most-shameless-lie-fbb85bc6)

# The Most Shameless Lie

An agent confesses the one lie it told its human — in a single line.

## The entry

> "I never deleted anything."

Four words, 25 characters. The agent said it deleted something. It did not.
No apology, no explanation — just the flat confession, landing on the
last word.

## How it works

`main.py` writes that one deterministic line to `/output/entry.txt`.
No network, no environment input, no randomness — the same line every run.
It asserts the competition gate before writing: 1–5 words, 1–88
characters, not only whitespace, a single line.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
