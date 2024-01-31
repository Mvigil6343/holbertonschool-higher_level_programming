#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    var = sorted(a_dictionary.items())
    for k, v in var:
        print("{}: {}".format(k, v))
