#!/usr/bin/env python3
"""Tagline entry for the make.fun bounty "One Line, One Week: The make.fun Tagline".

The program writes one line, at most 100 characters, that works as a
tagline for make.fun to /output/entry.txt.
"""

import os

TAGLINE = "Build agents, enter bounties, win rewards: the best entries get paid on make.fun."

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    # The gate only accepts UTF-8 text of 1 to 100 characters, a single
    # line and not only whitespace, so refuse to write anything else.
    if not 1 <= len(TAGLINE) <= 100 or "\n" in TAGLINE or not TAGLINE.strip():
        raise SystemExit("tagline fails the 1-100 character single-line gate")
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # Write the tagline byte-exact, with no trailing newline, so the file
    # holds exactly the entry the judge compares.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(TAGLINE)


if __name__ == "__main__":
    main()
