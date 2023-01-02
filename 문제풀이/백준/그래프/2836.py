import sys
input = sys.stdin.readline

H, W = map(int, input().split())
time = 0
count = 0
prev = 0
m = []
visited = [[False for _ in range(W)] for _ in range(H)]
dir = [(1,0), (0, 1), (-1, 0), (0, -1)]

for y in range(H):
  m.append(list(map(int, input().split(' '))))

def bfs(y,x):
  visited[y][x] = True

  queue = []
  queue.append((y,x))

  while queue:
    y,x = queue.pop()

    for d in dir:
      dy, dx = d
      ny, nx = y + dy, x + dx

      if ny >= H or ny < 0: continue
      if nx >= W or nx < 0: continue
      if visited[ny][nx]: continue

      visited[ny][nx] = True

      if m[ny][nx] == 0:
        queue.append((ny,nx))
      
      if m[ny][nx] == 1:
        m[ny][nx] = 2

while True:
  for y in range(H):
    for x in range(W):
      visited[y][x] = False
      if m[y][x] == 2:
        m[y][x] = 0
      if m[y][x] == 1:
        count += 1

  if count == 0:
    break

  time += 1
  prev = count
  count = 0
  bfs(0,0)

print(time)
print(prev)