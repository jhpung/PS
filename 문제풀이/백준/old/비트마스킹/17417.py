import sys

input = sys.stdin.readline
ret = sys.maxsize

N = int(input())

a = [0] * 12
mp = [[] for _ in range(12)]
P = list(map(int, input().split()))
visited = [False] * 12
comp = [0] * 12


def dfs(idx, flag):
    cnt = 1
    sum = a[idx]

    st = []
    st.append(idx)
    visited[idx] = True

    while len(st):
        curr = st.pop()
        for next in mp[curr]:
            if comp[next] == flag and not visited[next]:
                cnt += 1
                sum += a[next]
                visited[next] = True
                st.append(next)
            else:
                continue

    return cnt, sum


for i in range(len(P)):
    a[i + 1] = P[i]

for i in range(1, N + 1):
    t = list(map(int, input().split()))
    for j in range(1, len(t)):
        mp[i].append(t[j])
        mp[t[j]].append(i)

# 마지막껀 1111111 과 같은 모양이라 한 선거구만 존재하기되므로 제건한다.
for i in range(1, (1 << N) - 1):
    comp = [0] * 12
    visited = [False] * 12
    idx1, idx2 = -1, -1

    for j in range(0, N):
        if i & (1 << j):
            comp[j + 1] = 1
            idx1 = j + 1
        else:
            idx2 = j + 1

    cnt1, sum1 = dfs(idx1, 1)
    cnt2, sum2 = dfs(idx2, 0)

    if cnt1 + cnt2 == N:
        ret = min(ret, abs(sum1 - sum2))

if ret == sys.maxsize:
    print(-1)
else:
    print(ret)
