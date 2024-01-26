#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    a = sorted(my_list)
    return (a[(len(my_list) - 1)])
