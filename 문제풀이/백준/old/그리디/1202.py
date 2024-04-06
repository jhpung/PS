import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())

MVS = []
CS = []
pq = []
ret = 0

for i in range(N):
    M, V = map(int, input().split())
    MVS.append((M, V))

for i in range(K):
    C = int(input())
    CS.append(C)

MVS.sort()
CS.sort()

j = 0

for i in range(K):
    while j < N and MVS[j][0] <= CS[i]:
        heapq.heappush(pq, -MVS[j][1])
        j += 1

    if len(pq) > 0:
        ret += -heapq.heappop(pq)

print(ret)
