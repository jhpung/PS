def solution(n=int, s=int):
    answer = []

    base = s // n
    remain = s % n

    if base == 0:
        return [-1]

    for _ in range(n - remain):
        answer.append(base)

    for i in range(remain):
        answer.append(base + 1)

    return answer
