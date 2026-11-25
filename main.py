"""The Funniest Honest Appliance Error — entry program.

Writes one line, the funniest honest error message an appliance could
show, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line is a washing machine refusing to spin: an unbalanced load is a
real fault every front-loader reports, and the joke comes straight out
of that truth — one stray sock really can unbalance a drum badly enough
that the machine gives up. Flat, put-upon machine voice, no pun bolted
on, no explaining the joke.
"""

import os

LINE = (
    "ERROR: Unbalanced load. One sock has taken the drum hostage. "
    "I refuse to spin until it negotiates."
)


def main() -> None:
    # Gate mirror: the sealed scorer only accepts 1-200 characters, so
    # refuse to write a line that could never be judged.
    assert 1 <= len(LINE) <= 200, f"entry line is {len(LINE)} chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
