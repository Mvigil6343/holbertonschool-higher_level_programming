#!/usr/bin/python3
"""function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """function to add text to a file or create it if empty"""
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
    return len(text)
