#!/usr/bin/python3
"Add all unique integers in a list"


def uniq_add(my_list=[]):
    result = 0
    for i in set(my_list):
        result += i
    return (result)
