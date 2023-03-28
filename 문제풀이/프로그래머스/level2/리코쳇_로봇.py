from collections import deque


def solution(board=list):
    hsize = len(board)
    wsize = len(board[0])
    answer = -1

    visited = [[None for _ in range(wsize)] for _ in range(hsize)]
    q = deque()

    for i in range(hsize):
        for j in range(wsize):
            if board[i][j] == 'R':
                q.append((i, j))
                visited[i][j] = 0

    while q:
        y, x = q.popleft()

        # 동 서 남 북
        ny, nx = y, x

        while True:
            nny = ny - 1
            if ny - 1 < 0 or board[ny][nx] == 'D':
                if visited[ny][nx]:
                    break

    return answer
