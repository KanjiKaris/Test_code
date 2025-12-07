#!/usr/bin/env python3
def password():

    user_input = input("Type in the password: ")
    if user_input == "Python is awesome":
        return"Access Granted"
    else:
        return "Access Denied"

print(password())
