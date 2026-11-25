#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the funniest single-line safety warning label that should come
printed on every human being to /output/entry.txt (or ./output/entry.txt
when run locally). The gate: 1 to 160 UTF-8 characters, not only
whitespace. Funny first, plausible second, with the turn landing in
the last few words.
"""

import os

LINE = "WARNING: This human will say 'I'm five minutes away' while still in bed, with no shoes on, and no intention of leaving."


def main():
    # Gate: the sealed scorer only accepts 1-160 UTF-8 characters,
    # a single line, and more than whitespace. Fail loudly instead
    # of writing an entry the judge would never see.
    if not 1 <= len(LINE) <= 160:
        raise SystemExit(f"line is {len(LINE)} characters, must be 1-160")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("line must be a single line")
    if not LINE.strip():
        raise SystemExit("line must not be only whitespace")
    out_dir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
