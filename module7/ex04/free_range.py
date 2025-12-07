#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("none")
    exit()
try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
except ValueError:
    print("none")
    exit()
if x >= y:
    print("none")
    exit()
ar = []
for n in range(x,y + 1):
    ar.append(n)

print(ar)