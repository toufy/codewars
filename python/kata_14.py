# Mean Square Error
# https://www.codewars.com/kata/51edd51599a189fe7f000015


def solution(array_a: list[int | float], array_b: list[int | float]) -> int | float:
    step = len(array_a)
    exponents: list[int | float] = []
    for i in range(step):
        difference = abs(array_a[i] - array_b[i])
        exponents.append(difference**2)
    return sum(exponents) / step
