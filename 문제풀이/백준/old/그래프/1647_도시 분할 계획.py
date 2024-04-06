import sys
input = sys.stdin.readline
N, M = map(int,input().split())

p = [i for i in range(N + 1)]

e = []
r = []

def find(a):
    if p[a] == a:
        return a
    
    p[a] = find(p[a])
    
    return p[a]

def union(a, b):
    ap = find(a)
    bp = find(b)
    
    if ap == bp:
        return
    elif ap > bp:
        p[bp] = ap
    else:
        p[ap] = bp
    

for _ in range(M):
    A, B, C = map(int, input().split())
    
    e.append((C, A, B))

e.sort(key=lambda x: x[0])

total = 0
largest = 0

for c, a, b in e:
    ap = find(a)
    bp = find(b)
    
    if ap == bp:
        continue
    
    union(a,b)
    r.append((c, a, b))
    total += c
    largest = max(c, largest)    
    if len(r) == N - 1:
        break
    
print(total - largest)