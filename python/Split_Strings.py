def solution(s: str):
    if len(s) % 2 != 0:
        s += "_"
    it = iter(s)
    return ["".join([i, j]) for i, j in zip(it, it)]
