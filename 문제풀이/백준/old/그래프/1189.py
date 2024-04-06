import sys

input = sys.stdin.readline

R, C, K = map(int,input().split())

m = []
result = [0 for _ in range(1000)]
visited = [[False for _ in range(C)] for _ in range(R)]
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def find(y, x, c):
  if y == 0 and x == C - 1:
    result[c] += 1
    return

  for dy, dx in dirs:
    ny, nx = y + dy, x + dx

    if ny < 0 or ny >= R: continue
    if nx < 0 or nx >= C: continue
    if visited[ny][nx]: continue
    if m[ny][nx] == 'T':
      continue

    visited[ny][nx] = True
    find(ny, nx, c + 1)
    visited[ny][nx] = False


for h in range(R):
  m.append(list(input()))


visited[R - 1][0] = True

find(R - 1, 0, 1)

print(result[K])

