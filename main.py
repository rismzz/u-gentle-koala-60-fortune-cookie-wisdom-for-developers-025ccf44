#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — writes one fortune to /output/entry.txt.

Deterministic, no network, no randomness: the chosen line is embedded
below as a literal and written verbatim. One line, one fortune: the code
does compile on the first try — just never your own. It reads like a
real fortune cookie and says something true about a developer's day.
"""

from pathlib import Path

TEXT = (
    "Your code will compile on the first try. "
    "Unfortunately, it will be someone else's code."
)


def main() -> None:
    # Gate: 1 to 120 Unicode code points, not only whitespace.
    assert 1 <= len(TEXT) <= 120, f"text is {len(TEXT)} code points"
    assert TEXT.strip(), "text must not be only whitespace"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
