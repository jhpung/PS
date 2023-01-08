import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())

m = []

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(N):
    m.append(list(map(int, input().split())))

ret = 0

while True:
    flag = False
    visited = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            queue = deque()
            queue.append((i, j))
            group = deque()
            group.append((i, j))

            visited[i][j] = True
            while queue:
                y, x = queue.popleft()
                # if visited[y][x]:
                #     continue

                # visited[y][x] = True

                for dy, dx in dirs:
                    ny, nx = y + dy, x + dx

                    if ny >= N or ny < 0 or nx >= N or nx < 0:
                        continue
                    if visited[ny][nx]:
                        continue

                    if L <= abs(m[y][x] - m[ny][nx]) <= R:
                        visited[ny][nx] = True
                        group.append((ny, nx))
                        queue.append((ny, nx))

            if len(group) > 1:
                flag = True
                num = 0
                for y, x in group:
                    num += m[y][x]
                num = num // len(group)
                for y, x in group:
                    m[y][x] = num
    if not flag:
        break
    ret += 1

print(ret)
