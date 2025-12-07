#!/usr/bin/env python3

import sys

def downcase_it(s):
    return s.lower()

args = sys.argv[1:]

if len(args) == 0:
    print("none")
    exit()

for p in args:
    print(downcase_it(p))