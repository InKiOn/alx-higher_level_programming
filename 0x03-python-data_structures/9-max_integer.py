#!/usr/bin/python3
"""finds the biggest integer of a list"""


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    largest_int = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > largest_int:
            largest_int = my_list[i]
    return (largest_int)
