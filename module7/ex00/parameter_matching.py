#!/usr/bin/env python3

import sys
def main():
    if len(sys.argv) != 2:
        print("none")
        return
    param = sys.argv[1]
    answer = input("What was the parameter: ")
    if answer == param:
        print("Good job!")
    else:
        print("Nope, Sorry...")
if __name__=="_main_":
    main()

main()