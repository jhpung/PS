def solution(n=int):
    answer = 0
    n_count = bin(n).count('1')
    curr = n

    while True:
        curr += 1

        if bin(curr).count('1') == n_count:
            answer = curr
            break

    return answer
