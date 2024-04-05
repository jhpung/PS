import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    
    degrees = [-1] + [0 for _ in range(N)]
    dp = [0 for _ in range(N + 1)] 
    tree = defaultdict(list)
    parents = defaultdict(list)
    times = [None] + list(map(int, input().split()))
    
    for _ in range(K):
        x, y = map(int, input().split())
        
        tree[x].append(y)
        parents[y].append(x)
        degrees[y] += 1
    
    w = int(input())
    
    queue = []
    
    for index, item in enumerate(degrees):
        if item == 0:
            queue.append(index)

    for i in range(1, N + 1):
        x = queue.pop(0)
        
        if parents[x]:
            mx = 0 
            for p in parents[x]:
                mx = max(dp[p] + times[x], mx)
            dp[x] = mx
        else:
            dp[x] = times[x]
        
        if tree[x]:
            for next in tree[x]:
                degrees[next] -= 1
                
                if degrees[next] == 0:
                    queue.append(next)
    
    print(dp[w])