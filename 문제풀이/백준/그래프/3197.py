from collections import deque
import sys
input = sys.stdin.readline

swanQ = deque()
borderQ = deque()
waterQ = deque()
waterBorderQ = deque()

R, C = map(int, input().split())

mp = []
swan_visited = [[False for _ in range(C)] for _ in range(R)]
water_visited = [[False for _ in range(C)] for _ in range(R)]
dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
swan = None

for y in range(0, R):
    mp.append(list(input()))
    for x in range(0, C):
        if mp[y][x] == 'L':
            swan = (y, x)
            waterQ.append((y, x))
            water_visited[y][x] = True
        if mp[y][x] == '.':
            waterQ.append((y, x))
swanQ.append(swan)
swan_visited[swan[0]][swan[1]] = True
day = 0

while True:
    # print('-----', day, '-----')
    while swanQ:
        y, x = swanQ.popleft()

        for dy, dx in dirs:
            ny, nx = y + dy, x + dx

            if ny < 0 or ny >= R or nx < 0 or nx >= C:
                continue
            if swan_visited[ny][nx]:
                continue
            swan_visited[ny][nx] = True
            if mp[ny][nx] == 'X':
                borderQ.append((ny, nx))
                continue
            if mp[ny][nx] == '.':
                swanQ.append((ny, nx))
                continue
            if mp[ny][nx] == 'L':
                print(day)
                exit(0)
    # print(waterQ)
    while waterQ:
        y, x = waterQ.popleft()

        for dy, dx in dirs:
            ny, nx = y + dy, x + dx

            if ny < 0 or ny >= R or nx < 0 or nx >= C:
                continue
            if water_visited[ny][nx]:
                continue
            water_visited[ny][nx] = True
            if mp[ny][nx] == 'X':
                mp[ny][nx] = '.'
                waterBorderQ.append((ny, nx))
                continue
            if mp[ny][nx] == '.':
                waterQ.append((ny, nx))
                continue

    # for y in range(R):
    #     for x in range(C):
    #         print(mp[y][x], end="")
    #     print()

    swanQ = borderQ.copy()
    waterQ = waterBorderQ.copy()

    borderQ.clear()
    waterBorderQ.clear()
    day += 1
