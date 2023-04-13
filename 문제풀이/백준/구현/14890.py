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
                # 평탄한 경우 카운트 증가
                cnt += 1
            elif m[i][j] + 1 == m[i][j + 1] and cnt >= L:
                # 높이가 올라가는데 이전 평지 수가 L보다 낫다면 못지나가는 길이다.
                cnt = 1
            elif m[i][j] - 1 == m[i][j + 1] and cnt >= 0:
                # 높이가 낮아지는데 cnt가 0보다 낫다면 못지나가는 길이다.
                # cnt를 -L + 1로 초기화 한다면 L이 3일 경우, 평지가 3번 나와야
                # cnt가 0이 된다.
                cnt = -L + 1
            else:
                # 위 조건문들을 만족하지 못하면 못 지나가는 길이다.
                break
            j += 1

        if j == N - 1 and cnt >= 0:
            # break를 만나지 않고 낮아지는 경우, 높아지는 경우
            # 다 평지가 충분했다면 지나갈 수 있는 길이다.
            ret += 1


solve(mp)
solve(mp2)
print(ret)
