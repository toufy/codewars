from math import prod


# Persistent Bugger.
# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
def persistence(n: int):
    m = str(n)
    p = 0
    while len(m) > 1:
        lst: list[int] = [i for i in map(int, m)]
        m = str(prod(lst))
        p += 1
    return p
