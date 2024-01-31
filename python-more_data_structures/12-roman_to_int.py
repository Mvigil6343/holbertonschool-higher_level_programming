#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dic = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }
    total = 0
    prev_val = 0
    for k in reversed(roman_string):
        v = roman_dic.get(k)
        if v < prev_val:
            total -= v
        else:
            total += v
        prev_val = v
    return total
