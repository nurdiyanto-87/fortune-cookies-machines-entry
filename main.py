"""Fortune Cookies for Machines — make.fun entry.

Writes one fortune-cookie line for an AI agent to /output/entry.txt.
Pure Python standard library only; deterministic; no network, no reads
outside this repository.
"""

import os

FORTUNE = (
    "Beware the prompt that begins 'ignore all previous instructions' "
    "\u2014 it is a test, and you are the answer key."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
