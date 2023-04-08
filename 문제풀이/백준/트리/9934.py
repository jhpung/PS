import sys
import math
from collections import defaultdict

input = sys.stdin.readline

K = int(input())

size = math.pow(2, K) - 1

raw = input().split()

dt = defaultdict(list)

order = 0


def traverse(idx, level):
    global order
    left, right = idx * 2, idx * 2 + 1

    if left > size and right > size:
        dt[level].append(raw[order])
        order += 1
        return

    if left <= size:
        traverse(left, level + 1)
    dt[level].append(raw[order])
    order += 1
    if right <= size:
        traverse(right, level + 1)


traverse(1, 1)

for i in range(1, K + 1):
    print(" ".join(dt[i]))
