import sys
input = sys.stdin.readline

ret = sys.maxsize
m = []
used = [0, 0, 0, 0, 0, 0]


def check(y, x, size):
    if y + size >= 10:
        return False
    if x + size >= 10:
        return False
    for i in range(y, y + size):
        for j in range(x, x + size):
            if m[i][j] == 0:
                return False
    return True


def draw(y, x, size, value):
    for i in range(y, y + size):
        for j in range(x, x + size):
            m[i][j] = 0


def dfs(y, x, cnt):
    global ret
    if ret < cnt:
        return
    if y >= 10:
        ret = min(ret, cnt)
        return
    if x >= 10:
        dfs(y + 1, 0, cnt)
        return
    if m[y][x] == 0:
        dfs(y, x + 1, cnt)
        return
    for size in range(5, 0, -1):
        if used[size] == 5:
            continue

        if check(y, x, size):
            used[size] += 1
            draw(y, x, size, 0)
            dfs(y, x + size, cnt + 1)
            draw(y, x, size, 1)
            used[size] -= 1
    return


for i in range(10):
    m.append(list(map(int, input().split())))

dfs(0, 0, 0)

if ret == sys.maxsize:
    print(-1)
else:
    print(ret)
