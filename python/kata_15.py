# Next smaller number with the same digits
# https://www.codewars.com/kata/5659c6d896bc135c4c00021e


def next_smaller(n: int) -> int:
    digs = list(map(int, str(n)))[::-1]
    try:
        for pos, i in enumerate(digs.copy()):
            if digs[pos + 1] > i:
                big = digs[pos + 1]
                small = max(j for j in digs[: pos + 1] if j < digs[pos + 1])
                small_index = digs.index(small)
                digs[pos + 1] = small
                digs[small_index] = big
                digs = digs[: pos + 1][::-1] + digs[pos + 1 :]
                break
    except IndexError:
        return -1
    m = int("".join(map(str, digs[::-1])))
    if m < n and len(str(m)) == len(str(n)):
        return m
    return -1
