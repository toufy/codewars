import string


# Scramblies
# https://www.codewars.com/kata/55c04b4cc56a697bb0000048
def scramble(s1: str, s2: str):
    alphabet = list(string.ascii_lowercase)
    letters = set(s2)
    for char in alphabet:
        if char not in letters:
            s1 = s1.replace(char, "")
    return all(s1.count(char) >= s2.count(char) for char in letters)
