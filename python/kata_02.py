# Odd or Even?
# https://www.codewars.com/kata/5949481f86420f59480000e7


def odd_or_even(arr: list[int]):
    if sum(arr) % 2 == 0:
        return "even"
    return "odd"
