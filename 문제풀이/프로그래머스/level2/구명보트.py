from collections import deque


def solution(people=list, limit=int):
    answer = 0
    people.sort()
    dq = deque(people)

    while dq:

        if len(dq) < 2:
            answer += 1
            dq.pop()
            continue

        most_heavy = dq[-1]
        most_light = dq[0]

        if most_heavy + most_light <= limit:
            dq.pop()
            dq.popleft()
        else:
            dq.pop()
        answer += 1

    return answer
