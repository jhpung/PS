# 이 문제는 DP문제다.
# DP문제긴 한데, 재귀로 풀면 재귀 깊이 제한에 걸린다.

mem = [None for _ in range(100_000)]
mem[0] = 0
mem[1] = 1


def fibo(n: int):

    if n == 0:
        return 0

    elif n == 1:
        return 1

    if mem[n]:
        return mem[n]

    result = fibo(n-1) + fibo(n-2)
    mem[n] = result

    return result


def solution(n: int):
    answer = 0

    for i in range(0, n + 1):
        if i == 0:
            mem[i] = 0
            continue

        if i == 1:
            mem[i] = 1
            continue

        mem[i] = mem[i-1] + mem[i-2]

    return mem[i] % 1234567


print(solution(100_000))
