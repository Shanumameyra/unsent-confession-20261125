"""Unsent: The Micro-Confession Sprint.

Writes the two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, then the unsent message
itself, one line written exactly as it was typed, with no
explanation after it. Deterministic: the same bytes every run.
"""

import os

TO_LINE = "To: my driving instructor"
MESSAGE = (
    "i passed my test because you pretended not to see me stall "
    "at the roundabout, and i never told anyone, not even my wife, "
    "that my licence is built on your kindness."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = TO_LINE + "\n" + MESSAGE + "\n"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
