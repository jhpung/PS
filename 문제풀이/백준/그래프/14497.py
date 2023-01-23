import sys
from collections import deque
input = sys.stdin.readline

H, W = map(int, input().split())

x1, y1, x2, y2 = map(int, input().split())

x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1

mp = []

for i in range(H):
    mp.append(list(input()))


find = False
ret = 0
visited = [[False for _ in range(W)] for _ in range(H)]


def bfs(q):
    global find
    global ret
    global visited
    next = deque()

    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue

            if visited[nx][ny]:
                continue

            visited[nx][ny] = True
            if mp[nx][ny] == '1':
                mp[nx][ny] = '0'
                next.append((nx, ny))
                continue
            if mp[nx][ny] == '0':
                q.append((nx, ny))
                continue
            if mp[nx][ny] == '#':
                find = True
                break
    return next


q = deque()
visited[x1][y1] = True
q.append((x1, y1))

while not find:
    ret += 1
    q = bfs(q)


print(ret)
