def duplicate_count(text: str):
    s = text.lower()
    S1 = set(s)
    dups = sum([1 for i in S1 if s.count(i) > 1])
    return dups
