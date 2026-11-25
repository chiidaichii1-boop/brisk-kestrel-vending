"""One Line, One Minute: The Vending Machine Pickup Line Contest — make.fun entry.

Writes one pickup line, as if a vending machine were flirting with a
passing human, to /output/entry.txt.
"""

import os

LINE = (
    "Press B7 for the good stuff — I've got exact change, a full coil "
    "of snacks, and a crush on you that even my refund button can't fix."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
