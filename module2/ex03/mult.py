#!/usr/bin/env python3


def multiply():

    x= int(input("Enter the first number: "))
    y= int(input("Enter the second number: "))
    return x*y

result = multiply()
print(result)

if result == 0:
    print("The result is Positive and Negative")
elif result < 0:
    print("The result is Negative")
else:
    print("The result is Positive")
