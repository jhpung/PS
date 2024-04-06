import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N = int(input())

mp, mf, ms, mv = map(int, input().split())

table = []
ret = sys.maxsize
retd = defaultdict(list)

for i in range(N):
    p, f, s, v, c = map(int, input().split())

    table.append({
        "p": p,
        "f": f,
        "s": s,
        "v": v,
        "c": c
    })

for i in range(1 << N):
    p = f = s = v = sum = 0
    tv = []
    for j in range(N):
        if i & (1 << j):
            tv.append(j + 1)
            curr = table[j]
            p += curr["p"]
            f += curr["f"]
            s += curr["s"]
            v += curr["v"]
            sum += curr["c"]
        if p >= mp and f >= mf and s >= ms and v >= mv:
            if ret >= sum:
                ret = sum
                retd[ret].append(tv)

if ret == sys.maxsize:
    print(-1)
else:
    print(ret)
    retd[ret].sort()
    for item in retd[ret][0]:
        print(item, end=" ")
