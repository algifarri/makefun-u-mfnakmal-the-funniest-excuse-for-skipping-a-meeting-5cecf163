#!/usr/bin/env python3
"""make.fun entry: The Funniest Excuse for Skipping a Meeting.

Writes one razor-sharp excuse line (at most 200 characters) to
/output/entry.txt. Deterministic, stdlib-only, no network, no input.
"""

import os
from pathlib import Path

EXCUSE = (
    "Sorry, I have a conflict - I'm booked to do the actual work "
    "this meeting was called to discuss."
)
# The line is 95 characters: one tight sentence, no throat-clearing,
# and it lands the joke on the meeting itself, not on wifi or pets.


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        target = output_dir / "entry.txt"
    except OSError:
        target = Path("output") / "entry.txt"
        target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(EXCUSE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
