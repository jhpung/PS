import sys
from heapq import heappush, heappop
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())

in_degrees = [0 for _ in range(N + 1)]
mp = defaultdict(list)

result = []

for _ in range(M):
    a, b = map(int, input().split())
    
    mp[a].append(b)
    in_degrees[b] += 1


heap = []

for i in range(1, N + 1):
    if in_degrees[i] == 0:
        heappush(heap, i)
        
while heap:
    curr = heappop(heap)
    
    result.append(curr)
    
    for p in mp[curr]:
        in_degrees[p] -= 1
        
        if in_degrees[p] == 0:
            heappush(heap, p)
        
print(*result)