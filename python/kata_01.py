# Exes and Ohs
# https://www.codewars.com/kata/55908aad6620c066bc00002a
def xo(s: str):
    i = s.lower()
    return i.count("x") == i.count("o")
