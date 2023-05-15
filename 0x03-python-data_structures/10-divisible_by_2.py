#!/usr/bin/python3
"""finds all multiples of 2 in a list"""


def divisible_by_2(my_list=[]):
    multi_of_two = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multi_of_two.append(True)
        else:
            multi_of_two.append(False)
    return (multi_of_two)
