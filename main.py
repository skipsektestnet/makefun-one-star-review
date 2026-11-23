"""One-Star Review of Something Essential: writes the entry to /output/entry.txt.

The judge wants a deadpan one-star review of an everyday essential, with
the sharpest true grievance held straight, turning in the last few words.
Gravity is the perfect target: everyone relies on it, no one can fix it,
and it has genuinely dropped everything anyone has ever owned. The
complaint is filed in earnest, like a real review — it dropped my things,
it never apologised, and the turn lands at the very end: it has never
once offered to pick any of it up. Gravity cannot pick things up; that
is the whole joke, delivered deadpan, with no exclamation mark and no wink.

The entry text is assembled below from three fragments, joined with a
single space, so the sentence is built step by step and stays readable.
"""

import os

# The entry itself: one line, at most 160 characters.
# Kept as fragments so the sentence can be read and checked piece by piece.
ENTRY_PARTS = [
    "One star. Gravity has dropped everything I have ever owned",
    "and has never once apologised",
    "or offered to pick any of it up.",
]

# Joining with one space rebuilds the exact one-line entry.
ENTRY = " ".join(ENTRY_PARTS)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160


def validate_entry(text):
    """Check the entry before writing it anywhere."""
    # Guard: never submit a blank entry to the sealed gate.
    assert text, "entry must not be empty"
    assert not text.isspace(), "entry must not be blank"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} chars, got {len(text)}"
    )
    # The gate reads a single line: no newline may sneak into the entry.
    assert "\n" not in text, "entry must be a single line"
    # No stray leading/trailing whitespace: the gate reads the line as-is.
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    return text


def write_entry(text):
    """Write the validated entry to the output path."""
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print("wrote", OUTPUT_PATH, len(text), "chars")


def main():
    """Validate the entry, then write it out."""
    checked = validate_entry(ENTRY)
    write_entry(checked)


if __name__ == "__main__":
    main()
