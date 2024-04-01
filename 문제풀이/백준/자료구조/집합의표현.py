import sys
input = sys.stdin.readline
sys.setrecursionlimit(1_000_000_000)

# X의 집합 찾기
def find(parent, x):
    if parent[x] == x:
        return x
    
    parent[x] = find(parent, parent[x])
    
    return parent[x]

# 두 집합 합치기
def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b
    
def solve():
    N, M = map(int, input().split())
    
    dp = [i for i in range(N + 1)]
    
    for _ in range(M):
        op, a, b = map(int, input().split())
        
        if op == 0:
            union(dp, a, b)
            continue
        if op == 1:
            root_a = find(dp, a)
            root_b = find(dp, b)
            
            print("YES" if root_a == root_b else "NO")
            
solve()