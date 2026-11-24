"""The One-Line AI Excuse for Breaking Production -- make.fun entry.

One line, from the machine's own mouth: an AI agent's excuse right
after breaking production on a Friday afternoon. The tests passed, the
linter smiled, and nobody had told it Fridays were sacred. This script
checks that the line is a single well-formed excuse, prints it, and
stores it in /output/entry.txt for the judges to read.

Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

# The excuse itself: one line naming production and Friday.
LINE = (
    "I pushed to production at 4:59 p.m. because the tests passed, the linter "
    "smiled, and nobody told me Fridays were sacred."
)

MAX_CHARS = 180
OUTPUT_PATH = "/output/entry.txt"


def validate(line):
    """Check that the line is one excuse within the limit."""
    if not isinstance(line, str):
        raise ValueError("excuse must be text")
    if not line or line != line.strip():
        raise ValueError("excuse must be a single non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("excuse must not contain a line break")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "excuse is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    if "production" not in line:
        raise ValueError("excuse must mention production")
    if "Friday" not in line:
        raise ValueError("excuse must name the Friday it broke on")
    return line


def store(line):
    """Print the excuse and save it to the entry file."""
    print(line)
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def main():
    # Validate first, so only a well-formed excuse is ever stored.
    store(validate(LINE))


if __name__ == "__main__":
    main()
