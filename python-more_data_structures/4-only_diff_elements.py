#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_set = set()
    diff_set.update(set_1 - set_2)
    diff_set.update(set_2 - set_1)

    return diff_set
