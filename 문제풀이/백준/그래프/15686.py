import sys
import itertools
input = sys.stdin.readline

N, M = map(int, input().split())
cnt = 0
ret = sys.maxsize
m = []

for i in range(N):
    m.append(list(map(int, input().split())))

EMPTY = 0
HOUSE = 1
STORE = 2

# 치킨집, 일반 집 뽑아내기
stores = []
houses = []

for i in range(N):
    for j in range(N):
        if m[i][j] == EMPTY:
            continue
        if m[i][j] == STORE:
            stores.append((i, j))
            continue
        if m[i][j] == HOUSE:
            houses.append((i, j))
            continue

for combi in itertools.combinations(stores, M):
    sum = 0
    for house in houses:
        hy, hx = house
        min_house = sys.maxsize
        for store in combi:
            sy, sx = store
            dist = abs(hy - sy) + abs(hx - sx)
            min_house = min(min_house, dist)
        sum += min_house

    ret = min(sum, ret)

print(ret)
