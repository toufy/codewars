# Calculating with Functions
# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39

from typing import Callable


def zero(op: Callable[[int], int] | None = None):
    if op:
        x = op(0)
        return x
    return 0


def one(op: Callable[[int], int] | None = None):
    if op:
        x = op(1)
        return x
    return 1


def two(op: Callable[[int], int] | None = None):
    if op:
        x = op(2)
        return x
    return 2


def three(op: Callable[[int], int] | None = None):
    if op:
        x = op(3)
        return x
    return 3


def four(op: Callable[[int], int] | None = None):
    if op:
        x = op(4)
        return x
    return 4


def five(op: Callable[[int], int] | None = None):
    if op:
        x = op(5)
        return x
    return 5


def six(op: Callable[[int], int] | None = None):
    if op:
        x = op(6)
        return x
    return 6


def seven(op: Callable[[int], int] | None = None):
    if op:
        x = op(7)
        return x
    return 7


def eight(op: Callable[[int], int] | None = None):
    if op:
        x = op(8)
        return x
    return 8


def nine(op: Callable[[int], int] | None = None):
    if op:
        x = op(9)
        return x
    return 9


def plus(n: int) -> object:
    fn: Callable[[int], int] = lambda m: m + n
    return fn


def minus(n: int) -> object:
    fn: Callable[[int], int] = lambda m: m - n
    return fn


def times(n: int) -> object:
    fn: Callable[[int], int] = lambda m: m * n
    return fn


def divided_by(n: int) -> object:
    fn: Callable[[int], int] = lambda m: m // n
    return fn
