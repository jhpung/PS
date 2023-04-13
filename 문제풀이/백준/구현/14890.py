import sys
input = sys.stdin.readline

MAX_N = 104
N, L = map(int, input().split())
ret = 0

mp = [[None for _ in range(MAX_N)] for _ in range(MAX_N)]
mp2 = [[None for _ in range(MAX_N)] for _ in range(MAX_N)]

for i in range(N):
    l = list(map(int, input().split()))
    for j in range(len(l)):
        mp[i][j] = l[j]
        # 세로도 가로로 통일해서 간단하게 만든다.
        mp2[j][i] = mp[i][j]


def solve(m: list):
    global ret
    for i in range(N):
        cnt = 1
        j = 0
        while j < N - 1:
            if m[i][j] == m[i][j + 1]:
                cnt += 1
            elif m[i][j] + 1 == m[i][j + 1] and cnt >= L:
                cnt = 1
            elif m[i][j] - 1 == m[i][j + 1] and cnt >= 0:
                cnt = -L + 1
            else:
                break
            j += 1
        if j == N - 1 and cnt >= 0:
            ret += 1


solve(mp)
solve(mp2)
print(ret)
