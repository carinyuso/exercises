#!/usr/bin/python3

try:
    print(1/0)
except ZeroDivisionError:
    raise ValueError
