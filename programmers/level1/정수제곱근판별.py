import math


def solution(n: int):
    x = math.sqrt(n)

    if not x.is_integer():
        return -1

    return math.pow(x + 1, 2)
