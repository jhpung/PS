import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
if N == K:
    print(0)
    exit(0)

MAX_LEN = 500_000

visited = [[-1 for _ in range(MAX_LEN + 4)] for _ in range(2)]

ok = False
turn = 1

q = deque()
q.append(N)
visited[0][N] = 1

while q:
    K = K + turn

    if K > MAX_LEN:
        break
    if visited[turn % 2][K] != -1:
        ok = True
        break

    size = len(q)

    for i in range(size):
        curr = q.popleft()
        for next in [curr + 1, curr - 1, curr * 2]:
            if next < 0 or next > MAX_LEN or visited[turn % 2][next] != -1:
                continue

            visited[turn % 2][next] = visited[(turn + 1) % 2][curr] + 1
            if next == K:
                ok = True
                break
            q.append(next)
        if ok:
            break
    if ok:
        break
    turn += 1

if ok:
    print(turn)
else:
    print(-1)
