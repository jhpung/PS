import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

SIZE = 100_001

ret = sys.maxsize
cnt = 0

dp = [-1 for _ in range(SIZE)]

queue = deque()

queue.append((N, 0))

dp[N] = 0

while queue:
    pos, time = queue.popleft()

    if dp[pos] != -1 and dp[pos] < time:
        continue
    dp[pos] = time

    if pos == K:
        if time < ret:
            ret = time
            cnt = 0
        if time == ret:
            cnt += 1
        if time > ret:
            continue

    if pos + 1 < SIZE:
        queue.append((pos + 1, time + 1))
    if pos - 1 >= 0:
        queue.append((pos - 1, time + 1))
    if pos * 2 < SIZE:
        queue.append((pos * 2, time + 1))

print(ret)
print(cnt)
