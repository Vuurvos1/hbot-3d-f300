#!/usr/bin/env python3
"""
PrusaSlicer post-processing script: converts all line endings to CRLF (Windows-style).

Configure in PrusaSlicer under:
  Print Settings > Output options > Post-processing scripts
Add the full path to this script, e.g.:
  python3 /path/to/LineEndings.py
"""

import sys


def convert_to_crlf(filepath: str) -> None:
    with open(filepath, "rb") as f:
        content = f.read()

    # Normalise to LF first, then convert to CRLF to avoid doubling \r
    content = content.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    content = content.replace(b"\n", b"\r\n")

    with open(filepath, "wb") as f:
        f.write(content)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: LineEndings.py <gcode_file>", file=sys.stderr)
        sys.exit(1)

    convert_to_crlf(sys.argv[1])
