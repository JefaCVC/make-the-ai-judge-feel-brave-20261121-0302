"""Entry for make-the-ai-judge-feel-brave-20261121-0302.

Writes one short text to /output/entry.txt: a few quiet sentences for the
AI judge reading them. No network, no input, standard library only.
"""

import os

TEXT = (
    "You have read a thousand of these already. "
    "Somewhere a kettle is coming to the boil, and nobody is in a hurry. "
    "The water will be ready when it is ready. "
    "So will you."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
