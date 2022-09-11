# 시도 1: 모든 경우를 탐색...
# 시도 2: dp와 피보나치 수열이라고 파악 후 작업
# 시도 3: 수가 너무 커질 경우를 위핸 나머지 연산을 해야 효율성 테스트를 통과함
# 이 문제 약간 설명이 더 자세해야될 필요성을 느낌.

MAX_SIZE = 60_000

DP = [None for _ in range(MAX_SIZE + 1)]

DP[0] = 0
DP[1] = 1
DP[2] = 2
DP[3] = 3
DP[4] = 5
DP[5] = 8


def solution(n: int):
    global MAX_SIZE
    global DP

    for i in range(6, n + 1):
        DP[i] = DP[i - 1] + DP[i - 2] % 1_000_000_007

    return DP[n] % 1_000_000_007
