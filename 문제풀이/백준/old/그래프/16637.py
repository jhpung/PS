import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
ret = -10000000000


def calc(a, b, op):
    if op == '+':
        return a + b
    if op == '*':
        return a * b
    if op == '-':
        return a - b


def go(idx, num):
    global ret
    if idx == len(nums) - 1:
        ret = max(ret, num)
        return

    go(idx + 1, calc(num, nums[idx + 1], ops[idx]))
    if idx + 2 <= len(nums) - 1:
        tmp = calc(nums[idx + 1], nums[idx + 2], ops[idx + 1])
        go(idx + 2, calc(num, tmp, ops[idx]))


statement = list(input())

sums = [0 for _ in range(N)]

nums = []
ops = []

for i in range(N):
    if i % 2 == 0:
        nums.append(int(statement[i]))
    else:
        ops.append(statement[i])

go(0, nums[0])

print(ret)
