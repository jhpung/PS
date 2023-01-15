import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

SIZE = 100_001

ret = sys.maxsize
cnt = 0

visited = [-1 for _ in range(SIZE * 2)]
prev = [-1 for _ in range(SIZE * 2)]

queue = deque()

queue.append((N, 0))

visited[N] = 1

while queue:
    pos, time = queue.popleft()

    if pos == K:
        ret = time
        break

    for npos in [pos + 1, pos - 1, pos * 2]:
        if npos >= SIZE * 2 or npos < 0 or visited[npos] != -1:
            continue
        visited[npos] = visited[pos] + 1
        prev[npos] = pos
        queue.append((npos, time + 1))

print(ret)

i = K
li = [i]
while i != N:
    i = prev[i]
    li.append(i)

li.reverse()
for j in li:
    print(j, end=' ')
