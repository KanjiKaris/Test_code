#!/usr/bin/env python3

import sys

def shrink(s):
    print(s[:8])

def enlarge(s):
    while len(s) < 8:
        s += "z"
    print(s)
    
args = sys.argv[1:]
if len(args) ==0:
    print("none")
    exit()
for p in args:
    length = len(p)
    if length > 8:
        shrink(p)
    elif length < 8:
        enlarge(p)
    else:
        print(p)
