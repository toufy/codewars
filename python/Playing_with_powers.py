def dig_pow(n: int, p: int):
    m = str(n)
    lst: list[int] = []
    for i, j in enumerate(map(int, m)):
        lst.append(j ** (p + i))
    mT = sum(lst)
    if mT % n == 0:
        return int(mT / n)
    return -1
