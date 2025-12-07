#!/usr/bin/env python3
x = input("Give me a number: ")

num =  float(x)
if num.is_integer():
    print("This number is an interger.")
else:
    print("This number is a decimal.")