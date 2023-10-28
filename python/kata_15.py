# Next bigger number with the same digits
# https://www.codewars.com/kata/55983863da40caa2c900004e


def next_bigger(n: int) -> int:
    digs = list(map(int, str(n)))[::-1]
    try:
        for pos, i in enumerate(digs.copy()):
            if digs[pos + 1] < i:
                small = digs[pos + 1]
                big = min(j for j in digs[: pos + 1] if j > digs[pos + 1])
                big_index = digs.index(big)
                digs[pos + 1] = big
                digs[big_index] = small
                digs = digs[: pos + 1][::-1] + digs[pos + 1 :]
                break
    except IndexError:
        return -1
    m = int("".join(map(str, digs[::-1])))
    if m > n and len(str(m)) == len(str(n)):
        return m
    return -1
