import sys
input = sys.stdin.readline

# 1 <= N <= 10,000, 1 <= M <= 100,000
N, M = map(int, input().split())
g = [[] for _ in range(N + 1)]
counts = [0 for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
mx = 0

def bfs(src):
  count = 1

  queue = [src]
  
  visited[src] = True

  while queue:
    curr = queue.pop()

    for next in g[curr]:
      if visited[next]:
        continue
      visited[next] = True

      count += 1
      queue.append(next)
  
  return count

for i in range(M):
  A, B = map(int, input().split())

  g[B].append(A)

for i in range(1, N + 1):
  for j in range(0, N + 1):
    visited[j] = False

  counts[i] = bfs(i)

  mx = max(mx, counts[i])


for i in range(1, N + 1):
  if counts[i] == mx:
    print(i, end =' ')