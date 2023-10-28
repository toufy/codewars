# Split Strings
# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001


def solution(s: str):
    if len(s) % 2 != 0:
        s += "_"
    it = iter(s)
    return ["".join([i, j]) for i, j in zip(it, it)]
