import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())

m = []

WALL = '#'
EMPTY = '.'
START = 'J'
FIRE = 'F'

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

queue = deque()
fire = deque()
queue_time_table = [[-1 for _ in range(C)] for _ in range(R)]
fire_time_table = [[-1 for _ in range(C)] for _ in range(R)]

for i in range(R):
    m.append(list(input()))

for i in range(R):
    for j in range(C):

        if m[i][j] == START:
            queue.append((i, j))
            queue_time_table[i][j] = 0
        if m[i][j] == FIRE:
            fire.append((i, j))
            fire_time_table[i][j] = 0

while fire:
    y, x = fire.popleft()

    for dy, dx in dirs:
        ny, nx = y + dy, x + dx

        if 0 > ny or ny >= R or 0 > nx or nx >= C:
            continue
        if fire_time_table[ny][nx] != -1:
            continue
        if m[ny][nx] == WALL:
            continue
        fire.append((ny, nx))
        fire_time_table[ny][nx] = fire_time_table[y][x] + 1

while queue:
    y, x = queue.popleft()
    for dy, dx in dirs:
        ny, nx = y + dy, x + dx

        if 0 > ny or ny >= R or 0 > nx or nx >= C:
            print(queue_time_table[y][x] + 1)
            exit(0)
        if queue_time_table[ny][nx] != -1:
            continue
        if fire_time_table[y][x] != -1 and queue_time_table[y][x] + 1 >= fire_time_table[ny][nx]:
            continue
        if m[ny][nx] == WALL:
            continue

        queue.append((ny, nx))
        queue_time_table[ny][nx] = queue_time_table[y][x] + 1

print("IMPOSSIBLE")
