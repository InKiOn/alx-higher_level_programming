#!/usr/bin/python3
"""Return true of false for character case"""
def islower(c):
    if ord(c) >= 97 || ord(c) <= 122:
        return True
    else:
        return False
