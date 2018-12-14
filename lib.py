import re


def extract_ints(a_string):
    return tuple(map(int, re.findall(r'-?\d+', a_string)))
