#!/usr/bin/python3
"""Prints the last digit of a number"""
def print_last_digit(number):
    i = abs(number) % 10
    print(f"{i}")
    return (i)
