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

def get_cost(a,b):
    return min([abs(a['x'] - b['x']), abs(a['y'] - b['y']), abs(a['z'] - b['z'])])

def solve():
    result = 0
    N = int(input())
    
    xs = []
    ys = []
    zs = []
    
    for i in range(N):
        x, y, z = map(int, input().split())
        xs.append((x, i))    
        ys.append((y, i))
        zs.append((z, i))
    
    xs.sort()
    ys.sort()
    zs.sort()
    
    edges = []
    
    
    for i in range(N - 1):
        xv1, xv2 = xs[i], xs[i+1]
        x_cost = abs(xv1[0] - xv2[0])
        
        yv1, yv2 = ys[i], ys[i+1]
        y_cost = abs(yv1[0] - yv2[0])
        
        zv1, zv2 = zs[i], zs[i + 1]
        z_cost = abs(zv1[0] - zv2[0])
        
        edges.append((x_cost, xv1[1], xv2[1]))
        edges.append((y_cost, yv1[1], yv2[1]))
        edges.append((z_cost, zv1[1], zv2[1]))
    
    edges.sort()
    dp = [i for i in range(N + 1)]
    for cost, a, b in edges:
        root_a = find(dp, a)
        root_b = find(dp, b)
        
        if root_a == root_b:
            continue
        
        union(dp, a, b)
        result += cost   
    
    print(result)
            
    
solve()