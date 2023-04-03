from collections import defaultdict


def solution(input_string):
    answer = ""
    dic = defaultdict(int)

    last = None
    for ch in input_string:

        if last is None:
            last = ch
            dic[ch] += 1
            continue

        if ch == last:
            continue

        if ch != last:
            last = ch
            dic[ch] += 1
            continue

    for ch in range(ord('a'), ord('z') + 1):
        if dic[chr(ch)] >= 2:
            answer = answer + chr(ch)

    return answer if len(answer) else "N"
