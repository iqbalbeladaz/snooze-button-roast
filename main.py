#!/usr/bin/env python3
"""Fire Drill in an Empty Building — Snooze Button Roast entry.

Writes one line roasting an alarm clock that rings at 6 AM on a Saturday
to /output/entry.txt. Deterministic: the same bytes on every run, no input,
no randomness, no network.

The roast: the alarm is a fire drill in a building nobody works in
anymore — loud, pointless, and weirdly proud of itself. The humour comes
from the mismatch: a device built for urgency, performing its emergency
routine for an audience of nobody, on the one morning nobody needs it,
and doing it with pride. It is not "I hate mornings" and it is not "who
invented the alarm clock" — it is a fire drill with no building, no fire,
and no one to save. The punchline lands in the last few words.
"""

from pathlib import Path

ENTRY = (
    "My alarm clock rings at 6 AM on Saturday like a fire drill in a building "
    "nobody works in anymore \u2014 loud, pointless, and weirdly proud of itself.\n"
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space, and a single line. Validate before writing so a
# bad line can never reach the gate: refuse anything that would fail it.
def validate(entry: str) -> str:
    text = entry.strip()
    assert text, "entry must not be only white space"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 characters, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    return text


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(validate(ENTRY) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
