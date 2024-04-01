import sys
input = sys.stdin.readline
sys.setrecursionlimit(1_000_000_000)


def find(parent, x):
    if parent[x] == x:
        return x
    
    parent[x] = find(parent, parent[x])
    
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

def solve():
    answer = 0
    
    V, E = map(int, input().split())
    
    dp = [i for i in range(V + 1)]
    edges = []
    
    for _ in range(E):
        a, b, c = map(int, input().split())
        
        edges.append((c, a, b))
    
    edges.sort()
    
    for c, a, b in edges:
        if find(dp, a) == find(dp, b):
            continue
        
        answer += c
        union(dp, a, b)
        
    print(answer)
    
solve()