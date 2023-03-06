def zero(op: object | None = None):
    if callable(op):
        x: int = op(0)
        return x
    return 0


def one(op: object | None = None):
    if callable(op):
        x: int = op(1)
        return x
    return 1


def two(op: object | None = None):
    if callable(op):
        x: int = op(2)
        return x
    return 2


def three(op: object | None = None):
    if callable(op):
        x: int = op(3)
        return x
    return 3


def four(op: object | None = None):
    if callable(op):
        x: int = op(4)
        return x
    return 4


def five(op: object | None = None):
    if callable(op):
        x: int = op(5)
        return x
    return 5


def six(op: object | None = None):
    if callable(op):
        x: int = op(6)
        return x
    return 6


def seven(op: object | None = None):
    if callable(op):
        x: int = op(7)
        return x
    return 7


def eight(op: object | None = None):
    if callable(op):
        x: int = op(8)
        return x
    return 8


def nine(op: object | None = None):
    if callable(op):
        x: int = op(9)
        return x
    return 9


def plus(n: int) -> int:
    return lambda m: m + n  # type: ignore


def minus(n: int) -> int:
    return lambda m: m - n  # type: ignore


def times(n: int) -> int:
    return lambda m: m * n  # type: ignore


def divided_by(n: int) -> int:
    return lambda m: m // n  # type: ignore
