#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        nlist = my_list.copy()
        nlist[idx] = element
        return nlist
    else:
        return my_list
