from collections import defaultdict
import math


def solution(n, words):
    d = defaultdict(bool)

    for turn in range(len(words)):
        word = words[turn]

        if turn == 0:
            prev = word
            d[word] = True
            continue

        if prev[-1] != word[0]:
            return [turn % n + 1, (turn // n) + 1]

        if d[word]:
            return [turn % n + 1, (turn) // n + 1]

        d[word] = True

        prev = word

    return [0, 0]
