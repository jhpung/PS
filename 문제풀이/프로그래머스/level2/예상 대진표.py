import math


def solution(n, a, b):
    if b < a:
        b, a = a, b

    answer = 1

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    while answer < (math.log(n, 2)):
        if a % 2 == 1 and b % 2 == 0 and b - a == 1:
            print(a, b)
            return answer
        print(a, b, answer)
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)

        answer += 1

    return answer


print(solution(2, 1, 2))
