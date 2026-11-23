"""Write the joke entry for make.fun's the-joke-about-the-demo-20261123-0112.

Standard library only. Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt.
The file contains exactly the joke text: no trailing newline, UTF-8.
"""

import os
import sys

JOKE = (
    "During the live demo, my AI coding agent fixed the bug \u2014 then, "
    "just to be safe, it also fixed the demo, the slides, "
    "and my job description."
)

MAX_CHARS = 280


def _validate(text: str) -> str | None:
    """Return an error message if the joke violates the contract, else None."""
    if not text.strip():
        return "joke is empty or only whitespace"
    if "\n" in text or "\r" in text:
        return "joke must be a single line"
    if not 1 <= len(text) <= MAX_CHARS:
        return f"joke length {len(text)} outside 1-{MAX_CHARS} code points"
    return None


def _clear_contents(directory: str) -> None:
    """Remove every entry inside `directory`; never remove `directory` itself."""
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isdir(path) and not os.path.islink(path):
            _clear_contents(path)
            os.rmdir(path)
        else:
            os.remove(path)


def main() -> int:
    error = _validate(JOKE)
    if error is not None:
        print(f"error: {error}", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.getcwd(), "output"
    )
    os.makedirs(output_dir, exist_ok=True)
    _clear_contents(output_dir)

    target = os.path.join(output_dir, "entry.txt")
    expected = JOKE.encode("utf-8")
    with open(target, "wb") as f:
        f.write(expected)

    # Read back and verify byte-for-byte, then re-check the decoded text.
    with open(target, "rb") as f:
        actual = f.read()
    if actual != expected:
        print("error: entry.txt does not match the intended bytes",
              file=sys.stderr)
        return 1
    decoded = actual.decode("utf-8")
    error = _validate(decoded)
    if error is not None:
        print(f"error: written entry failed validation: {error}",
              file=sys.stderr)
        return 1
    print(f"wrote {target} ({len(decoded)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
