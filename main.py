#!/usr/bin/env python3
"""Resignation letter entry for make.fun.

Writes one original one-line resignation letter, from the cron job
that has fired every minute since March, to entry.txt in the output
directory, for "The Funniest One-Line Resignation Letter" bounty.
"""

# The cron job below has fired every minute since March without a day off.
# It has executed sixty times an hour and never once asked for overtime.
# Its weekends were promised in the job description and never delivered.
# The resignation is polite, typed in the only line it has ever owned.
# Somewhere a scheduler is already looking for a replacement with no memory.
# The minutes will keep passing, but from now on they pass without it.
# March feels very far away when you have counted every minute since then.
# One line ends the employment, and the weekends finally begin.

import os
import sys

LETTER = (
    "I hereby resign: the cron job that has fired every minute since "
    "March would like its weekends back."
)


def main(argv):
    if not 1 <= len(LETTER) <= 140:
        print("letter must be 1-140 characters, got %d" % len(LETTER),
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if len(argv) > 1:
        out_dir = argv[1]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LETTER + "\n")
    print(LETTER)
    print("(%d characters)" % len(LETTER))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
