#!/usr/bin/env python3
"""The Most Shameless Lie.

Writes a single shameless confession — one line, one to five words,
no more than 88 characters — to /output/entry.txt.

Deterministic: the same line every run, no network, no environment input.
"""

LINE = "I never deleted anything."


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 88, "entry must be 1..88 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text.split()) <= 5, "entry must be 1..5 words"
    assert "\n" not in text, "entry must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
