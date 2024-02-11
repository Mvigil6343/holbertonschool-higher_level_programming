#!/usr/bin/python3
""""function that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """function that writes on a file"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    return len(text)
