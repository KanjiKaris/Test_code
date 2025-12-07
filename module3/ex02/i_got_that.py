#!/usr/bin/env python3

response = input("What can I do for you? : ")
while True:
    response = input("I got that! Anything else? : ")
    if response.strip().upper() == "STOP":
            break