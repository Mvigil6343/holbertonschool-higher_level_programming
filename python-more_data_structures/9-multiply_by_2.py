#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ndict = a_dictionary.copy()
    for i in ndict:
        ndict[i] *= 2
    return ndict
