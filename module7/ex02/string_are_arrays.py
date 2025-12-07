#!/usr/bin/env python3

import sys
if len(sys.argv) != 2:
    print("none")
    exit()

text = sys.argv[1]
count = 0

for ch in text:
    if ch == "z":
        print("z", end="")
        count += 1
if count == 0:
    print("none")
    