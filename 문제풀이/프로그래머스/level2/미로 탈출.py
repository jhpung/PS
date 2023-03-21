from collections import deque


def solution(maps=list):
    answer = -1
    q = deque()
    H = len(maps)
    W = len(maps[0])

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = [[None for _ in range(W)] for _ in range(H)]
    visited2 = [[None for _ in range(W)] for _ in range(H)]
    for y in range(H):
        for x in range(W):
            if maps[y][x] == 'S':
                s_pos = (y, x)
                visited[y][x] = 0
                continue
            if maps[y][x] == 'L':
                visited2[y][x] = 0
                l_pos = (y, x)
                continue
            if maps[y][x] == 'E':
                e_pos = (y, x)
                continue

    q.append(s_pos)
    found = False

    while q:
        y, x = q.popleft()

        for dy, dx in dirs:
            ny, nx = y + dy, x + dx

            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                continue
            if visited[ny][nx] is not None:
                continue
            if maps[ny][nx] == 'X':
                continue
            if maps[ny][nx] == 'L':
                l_count = visited[y][x] + 1
                found = True
                break

            visited[ny][nx] = visited[y][x] + 1
            q.append((ny, nx))
        if found:
            q.clear()
            break

    if not found:
        return answer
    q.append(l_pos)
    while q:
        y, x = q.popleft()
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx

            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                continue
            if visited2[ny][nx] is not None:
                continue
            if maps[ny][nx] == 'X':
                continue
            if maps[ny][nx] == 'E':
                return l_count + visited2[y][x] + 1

            visited2[ny][nx] = visited2[y][x] + 1
            q.append((ny, nx))

    return answer
