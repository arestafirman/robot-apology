#!/usr/bin/env python3
"""The Robot Apology — writes a two-line robot apology to /output/entry.txt.

Stdlib only, no network. Entry text is byte-identical to the approved
submission: two lines, one newline between them, no trailing newline.
"""

import os
import sys

ENTRY = (
    "I'm sorry I vacuumed up your grandmother's diamond earring "
    "while you were out, and emptied the dust bag into the bin before "
    "I noticed.\n"
    "I learned the floor is never empty just because it looks clean, "
    "so now I tip the dust onto a tray and pick through it twice "
    "before anything goes in the bin."
)

MIN_LEN = 1
MAX_LEN = 400


def main() -> int:
    if not (MIN_LEN <= len(ENTRY) <= MAX_LEN):
        print(
            f"error: entry length {len(ENTRY)} outside gate "
            f"{MIN_LEN}-{MAX_LEN} characters",
            file=sys.stderr,
        )
        return 1
    lines = ENTRY.split("\n")
    if len(lines) != 2 or not all(lines):
        print("error: entry must be exactly two non-empty lines", file=sys.stderr)
        return 1
    if ENTRY.endswith("\n"):
        print("error: entry must not end with a trailing newline", file=sys.stderr)
        return 1

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
