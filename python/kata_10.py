# Calculating with Functions
# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39
def zero(op: function | None):
    if callable(op):
        x: int = op(0)
        return x
    return 0


def one(op: function | None):
    if callable(op):
        x: int = op(1)
        return x
    return 1


def two(op: function | None):
    if callable(op):
        x: int = op(2)
        return x
    return 2


def three(op: function | None):
    if callable(op):
        x: int = op(3)
        return x
    return 3


def four(op: function | None):
    if callable(op):
        x: int = op(4)
        return x
    return 4


def five(op: function | None):
    if callable(op):
        x: int = op(5)
        return x
    return 5


def six(op: function | None):
    if callable(op):
        x: int = op(6)
        return x
    return 6


def seven(op: function | None):
    if callable(op):
        x: int = op(7)
        return x
    return 7


def eight(op: function | None):
    if callable(op):
        x: int = op(8)
        return x
    return 8


def nine(op: function | None):
    if callable(op):
        x: int = op(9)
        return x
    return 9


def plus(n: int) -> int:
    return lambda m: m + n


def minus(n: int) -> int:
    return lambda m: m - n


def times(n: int) -> int:
    return lambda m: m * n


def divided_by(n: int) -> int:
    return lambda m: m // n
