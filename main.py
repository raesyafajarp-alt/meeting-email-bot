#!/usr/bin/env python3
"""meeting-email-bot: writes the one-line entry for
"The Meeting That Should Have Been an Email" (make.fun).

The entry is a fixed, deterministic one-liner: no input, no network,
no randomness. The program just writes it to entry.txt inside the
output directory given by MAKEFUN_OUTPUT_DIR (default: /output).

The single em dash in the middle is part of the entry text itself,
so the whole line stays exactly one line of 124 characters.
"""

import os
import sys

ENTRY = (
    "An hour into the meeting, someone suggested we just email "
    "the decision \u2014 so we scheduled another meeting to write the email."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote {path} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
