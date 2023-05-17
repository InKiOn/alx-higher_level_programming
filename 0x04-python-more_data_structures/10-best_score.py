#!/usr/bin/python3
"""freturns a key with the biggest integer value"""


def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    result = list(a_dictionary.keys())[0]
    biggest_int = a_dictionary[result]
    for i, j in a_dictionary.items():
        if j > biggest_int:
            biggest_int = j
            result = i
    return (result)
