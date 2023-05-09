#!/usr/bin/python3
"""Print reverse alphabet in alternating case"""
n = 0
for a in range(ord('z'), ord('a') - 1, -1):
    print(f"{chr(a - i)}", end="")
    n = 32 if n == 0 else 0
