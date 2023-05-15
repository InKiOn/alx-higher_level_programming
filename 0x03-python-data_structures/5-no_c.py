#!/usr/bin/python3
"""Removes all characters c and C"""


def no_c(my_string):
    copied_list = [i for i in my_string if i != 'c' and i != 'C']
    return ("".join(copied_list))
