from collections import deque


def solution(board=list):

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    H = len(board)
    W = len(board[0])
    answer = -1

    visited = [[None for _ in range(W)] for _ in range(H)]

    q = deque()

    for y in range(H):
        for x in range(W):
            if board[y][x] == 'R':
                visited[y][x] = 0
                q.append((y, x, 0))

    while q:
        y, x, count = q.popleft()

        visited[y][x] = count
        if board[y][x] == 'G':
            return visited[y][x]
        # LEFT
        nx = x - 1
        while nx >= 0:
            if y == 1 and x == 6:
                print('nx', nx)
            if visited[y][nx]:
                if y == 1 and x == 6:
                    print('visited', y, nx)
                break
            if board[y][nx] == 'D' and visited[y][nx + 1] == None:
                q.append((y, nx + 1, count + 1))
                break
            if board[y][nx] == 'D':
                break
            if nx == 0 and visited[y][nx] == None:
                q.append((y, nx, count + 1))
                break
            nx -= 1
        # TOP
        ny = y - 1
        while ny >= 0:
            if visited[ny][x]:
                break
            if board[ny][x] == 'D' and visited[ny + 1][x] == None:
                q.append((ny + 1, x, count + 1))
                break
            if board[ny][x] == 'D':
                break
            if ny == 0 and visited[ny][x] == None:
                q.append((ny, x, count + 1))
                break
            ny -= 1
        # RIGHT
        nx = x + 1
        while nx < W:
            if visited[y][nx]:
                break
            if board[y][nx] == 'D' and visited[y][nx - 1] == None:
                q.append((y, nx - 1, count + 1))
                break
            if board[y][nx] == 'D':
                break
            if nx == W - 1 and visited[y][nx] == None:
                q.append((y, nx, count + 1))
                break
            nx += 1
            # BOTTOM
        ny = y + 1
        while ny < H:
            if visited[ny][x]:
                break
            if board[ny][x] == 'D' and visited[ny - 1][x] == None:
                q.append((ny - 1, x, count + 1))
                break
            if board[ny][x] == 'D':
                break
            if ny == H - 1 and visited[ny][x] == None:
                q.append((ny, x, count + 1))
                break
            ny += 1
    return answer
