import math


def solution(absolutes: list, signs: list):
    answer = 0
    for i in range(len(absolutes)):
        sign = signs[i]

        num = absolutes[i] * (+1 if sign else -1)
        answer = answer + num

    return answer
