import sys
from collections import defaultdict

input = sys.stdin.readline

N, M, H = map(int, input().split())

visited = [[False for _ in range(34)] for _ in range(34)]
ret = sys.maxsize

def check():
    for i in range(1, N + 1):
        start = i
        for j in range(1, H + 1):
            if visited[j][start]:
                start += 1
            elif visited[j][start-1]:
                start -= 1
        if start != i:
            return False
    return True

def go(here=int, cnt=int):
    global ret

    # print(here, cnt)
    if cnt > 3 or cnt >= ret:
        return
    if check():
        # print('good')
        ret = min(ret, cnt)
        return
    for i in range(here, H + 1):
        for j in range(1, N + 1):
            if visited[i][j] or visited[i][j-1] or visited[i][j+1]:
                continue
            visited[i][j] = True
            go(i, cnt + 1)
            visited[i][j] = False



for i in range(M):
    a,b = map(int, input().split())
    visited[a][b] = True

go(1,0)

if ret == sys.maxsize:
    print(-1)
else:
    print(ret)