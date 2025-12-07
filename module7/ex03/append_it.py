#!/usr/bin/env python3

import sys
args = sys.argv[1:]

if len(sys.argv) == 0:
    print("none")
    exit()

for p in args:
    if p.endswith("ism"):
        continue
    print(p + "ism")