"""One Word, First Thought — a make.fun entry.

Writes exactly one word to /output/entry.txt: the first word that comes
to mind. No topic, no framing — just the word.
"""

import os

LINE = "Again"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
