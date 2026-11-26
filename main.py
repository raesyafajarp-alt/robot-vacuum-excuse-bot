#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse entry.

When run, writes a single original one-line excuse a robot vacuum gives
for missing a spot to /output/entry.txt. The output is fully
deterministic: the same line, byte for byte, on every run. The joke works
because the vacuum treats the dust bunny as a paying tenant whose rights
it must respect, instead of admitting it missed the spot.
"""

import os

ENTRY = "I didn't miss that spot \u2014 the dust bunny under the sofa pays rent, so I respect a tenant's rights."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
