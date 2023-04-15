from collections import defaultdict
from queue import PriorityQueue

n = int(input())
dt = defaultdict(PriorityQueue)

cur = 10001

for i in range(n):
    p, d = map(int, input().split())

    dt[d].put(p)

    cur = min(cur, d)

ret = 0

m = dt[cur].get()

ret += m
print('go')
print(ret)
