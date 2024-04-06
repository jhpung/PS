from collections import deque
import sys

h, w = map(int, input().rstrip().split())

board = [(sys.stdin.readline().rstrip()) for _ in range(h)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


mm = 1


def bfs(y, x):
    visited = [[-1 for _ in range(w)] for _ in range(h)]
    queue = deque()
    queue.append((y, x))
    visited[y][x] = 0
    m = 0
    while queue:
        cy, cx = queue.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < h and 0 <= nx < w:
                if visited[ny][nx] == -1 and board[ny][nx] == 'L':
                    visited[ny][nx] = visited[cy][cx] + 1
                    m = max(visited[ny][nx], m)
                    queue.append((ny, nx))
    return m


for y in range(h):
    for x in range(w):
        if board[y][x] == 'L':
            up, down = y - 1, y + 1
            if up >= 0 and down < h:
                if board[up][x] == 'L' and board[down][x] == 'L':
                    continue
            left, right = x - 1, x + 1
            if left >= 0 and right < w:
                if board[y][left] == 'L' and board[y][right] == 'L':
                    continue
            mm = max(bfs(y, x), mm)
        else:
            continue

print(mm)
