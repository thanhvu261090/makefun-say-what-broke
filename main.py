"""Write one honest, funny error line to /output/entry.txt.

Stdlib only, no network. The line is a single line of plain text naming
a real failure (the server ran out of memory) and telling the user what
to do next, with a twist a reader repeats out loud.
"""

import os

ENTRY = (
    "The server ran out of memory trying to remember what you asked it "
    "to remember. Refresh and ask it again, gently."
)


def check_entry(text):
    """Gate-check: 1-200 chars, single line, non-whitespace, UTF-8."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    text.encode("utf-8")
    return True


def main():
    check_entry(ENTRY)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("written entry does not match the entry text")
    check_entry(written)
    print("wrote %d chars to /output/entry.txt" % len(ENTRY))


if __name__ == "__main__":
    main()
