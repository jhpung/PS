import sys
from collections import deque

input = sys.stdin.readline

k = int(input())

signs = input().split()
check = [False for _ in range(10)]
ret = []


def good(prev=int, op=str, next=int):
    if op == '<':
        return prev < next
    if op == '>':
        return prev > next


def go(idx=int, num=str):
    if idx == k + 1:
        return ret.append(num)
    for i in range(10):
        if check[i]:
            continue
        if idx == 0 or good(int(num[idx - 1]), signs[idx - 1], i):
            check[i] = True
            go(idx + 1, num + str(i))
            check[i] = False


ret.sort()

go(0, "")

print(ret[-1])
print(ret[0])
