#!/usr/bin/python3
def no_c(my_string):
    nstr = ""
    for i in my_string:
        if i != 'C' and i != 'c':
            nstr += i
    return nstr
