#!/usr/bin/env python3
"""Last Text at One Percent — make.fun bounty entry.

Picture the scene: a phone on its final sliver of charge, screen
dimming, one last message to fire off before the lights go out.
It has spent years watching its owner. It knows things. This script
puts that farewell into the output file, exactly as the phone said it.
"""

import os
import sys

# The phone's parting words. Tight enough to squeeze into a single
# text, pointed enough that its owner will be thinking about it
# long after the screen goes black.
LINE = "1% left. i've seen things. your 3am searches. your ex's profile. 47 times. tell no one. goodbye."


def main() -> int:
    # Where does the entry live? The harness passes the directory in;
    # when someone runs this by hand we just use a sensible default.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # The message goes out verbatim — no newline at the end, no
    # padding, no decoration. Just the phone's last words.
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
