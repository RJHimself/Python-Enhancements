import re


def integers(string):
    numbers=re.findall(r'\d+', str(string))
    return list(map(int, numbers))
