from collections import deque
import sys


def solution(m=int, n=int, puddles=list):
    dirs = [(0, -1), (-1, 0)]
    dirs2 = [(0, 1), (1, 0)]
    puddle_map = [[None for _ in range(n + 1)] for _ in range(m + 1)]
    visited = [[None for _ in range(n + 1)] for _ in range(m + 1)]

    for puddle in puddles:
        x, y = puddle
        puddle_map[x][y] = True

    visited[1][1] = 1

    q = deque()
    q.append((1, 2))
    q.append((2, 1))

    while q:
        x, y = q.popleft()

        if visited[x][y]:
            continue

        cur = 0

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if nx < 1 or nx > m or ny < 1 or ny > n:
                continue

            if puddle_map[nx][ny]:
                continue

            if visited[nx][ny]:
                cur = (cur + visited[nx][ny]) % 1_000_000_007

        visited[x][y] = cur

        if x == m and y == n:
            return cur

        for dx, dy in dirs2:
            nx, ny = x + dx, y + dy

            if nx < 1 or nx > m or ny < 1 or ny > n:
                continue

            if puddle_map[nx][ny]:
                continue

            if not visited[nx][ny]:
                q.append((nx, ny))
    return 0
