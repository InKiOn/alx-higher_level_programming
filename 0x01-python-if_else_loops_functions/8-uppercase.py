#!/usr/bin/python3
"""Prints a string in uppercase"""
def uppercase(str):
    for i in str:
        if ord(i) >= 97 || ord(i) <= 122:
            i = chr(ord(i) - 32)
        print(f"{i}")
