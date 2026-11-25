#!/usr/bin/env python3
"""The Absurd Clause Contest entry.

Writes one absurd clause, hidden deep inside a terms-of-service
agreement, to /output/entry.txt. Stdlib only, Python 3.13.
"""

import os

CLAUSE = (
    "User agrees that all time spent thinking about the Service, "
    "including during sleep, shall be billed at our standard hourly "
    "rate, rounded up to the nearest decade."
)


def main() -> None:
    text = CLAUSE.strip()
    assert text, "clause must not be blank"
    assert len(text) <= 200, (
        f"clause is {len(text)} characters, over the 200-character limit"
    )
    assert "\n" not in text, "clause must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and verify what the grader will see.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry.txt does not match the clause"
    assert 1 <= len(written) <= 200, "written entry is out of bounds"
    print(text)


if __name__ == "__main__":
    main()
