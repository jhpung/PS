# DP, BFS
import math
import sys
from collections import deque
from itertools import combinations

inf = sys.maxsize

input = sys.stdin.readline

N = int(input())

remains = list(map(int, input().split()))

if len(remains) == 2:
    remains.append(0)
if len(remains) == 1:
    remains.append(0)
    remains.append(0)
dp = [[[-1 for _ in range(64)] for _ in range(64)] for _ in range(64)]
visited = [[[-1 for _ in range(64)] for _ in range(64)] for _ in range(64)]

cases = [
    (9, 3, 1),
    (9, 1, 3),
    (3, 1, 9),
    (3, 9, 1),
    (1, 3, 9),
    (1, 9, 3),
]

[one, two, three] = remains
queue = deque([(one, two, three)])
visited[one][two][three] = 1

while queue:
    a, b, c = queue.popleft()
    if visited[0][0][0] != -1:
        break

    for da, db, dc in cases:
        na = max(a - da, 0)
        nb = max(b - db, 0)
        nc = max(c - dc, 0)

        if visited[na][nb][nc] != -1:
            continue

        visited[na][nb][nc] = visited[a][b][c] + 1
        queue.append((na, nb, nc))

print(visited[0][0][0] - 1)
