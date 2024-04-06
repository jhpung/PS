import sys
from collections import defaultdict, deque
from heapq import heappush, heappop

input = sys.stdin.readline

def dijkstra(start: int, end: int, edges: defaultdict, dp: list):
    heap = []
    dp[start] = 0

    heappush(heap, (0, start))
    
    while heap:
        distance, curr = heappop(heap)
    
        if dp[curr] < distance:
            continue
        
        for next_cost, next in edges[curr]:
            next_distance = distance + next_cost
            if next_distance > dp[next]:
                continue
            
            dp[next] = next_distance
            heappush(heap, (next_distance, next))
    
def solve():
    result = 0
    
    N, M, X = map(int, input().split())
    
    gp = defaultdict(list)
    
    for _ in range(M):
        s, e, c = map(int, input().split())
        
        gp[s].append((c, e))
    
    for i in range(1, N + 1):
        curr_result = 0
        
        dp = [sys.maxsize for _ in range(N + 1)]

        dijkstra(i, X, gp, dp)
        curr_result += dp[X]
        
        dp = [sys.maxsize for _ in range(N + 1)]
        
        dijkstra(X, i, gp, dp)
        curr_result += dp[i]
        
        result = max(result, curr_result)
    
    print(result)
        
solve()