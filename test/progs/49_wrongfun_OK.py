def f(x : int) -> int:
    """"""
    return x + 1


def h(y : int) -> int:
    """"""
    return f(y) * 2

assert f(4) == 5
assert f(4) == 5
assert h(2) == 6
