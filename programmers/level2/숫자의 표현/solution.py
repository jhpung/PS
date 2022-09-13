import math


def solution(n: int):
    answer = 1

    for i in range(1, math.ceil(n / 2) + 1):
        acc = i

        for j in range(i + 1, math.ceil(n / 2) + 2):
            if acc + j == n:
                answer = answer + 1
                break

            if acc + j < n:
                acc = acc + j
                continue
            if acc + j > n:
                break

    return answer


print(solution(15))
