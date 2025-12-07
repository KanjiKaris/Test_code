#!/usr/bin/env python3

x = int(input("Enter a number less than 25 \n"))
if x < 25:
        i = x
        while i <= 25:
            print(f"Inside the loop, my valuable is: {i}")
            i += 1          
else:
    print("Error \n")
