import sys
import heapq

input = sys.stdin.readline

N = int(input())

pq = []

for i in range(N):
    score = float(input())

    heapq.heappush(pq, -score)
    if len(pq) == 8:
        heapq.heappop(pq)

pq.sort(reverse=True)

for i in range(7):
    cur = -pq[i]

    print(f'{cur:.3f}')
