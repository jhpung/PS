#
# 이문제는 그리디 문제다. 매 번 가장 작은 수와 가장 큰수를 구하면 최소값이 나온다.
#

import sys


def solution(A: list, B: list):
    answer = 0

    A.sort()
    B.sort()

    while A:
        bigger = A.pop(0)
        smaller = B.pop(-1)

        answer = answer + bigger * smaller

    return answer


print(solution([1, 4, 2], [5, 4, 4]))
