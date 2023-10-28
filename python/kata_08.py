# Counting Duplicates
# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1


def duplicate_count(text: str):
    s = text.lower()
    S1 = set(s)
    dups = sum([1 for i in S1 if s.count(i) > 1])
    return dups
