#!/usr/bin/env python3
"""news-image-20261125 entrypoint.

The graded artifact is the committed entry.png, rendered once by
paint_n25.py in this session. This entrypoint only copies that file to
/output/entry.png. It never re-renders: re-rendering in the grader would
break the byte-identical guarantee the entry depends on.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main():
    if not os.path.isfile(SRC):
        print("missing committed entry.png next to main.py", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    print("copied", SRC, "->", DST, os.path.getsize(DST), "bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
