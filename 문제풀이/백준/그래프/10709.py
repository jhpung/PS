import sys
input = sys.stdin.readline

H, W = map(int, input().split())

ret = [[-1 for _ in range(W)] for _ in range(H)]

for i in range(H):
  WW = list(input())

  for j in range(W):
    for k in range(j, -1, -1):
      if WW[k] == 'c':
        ret[i][j] = max(j - k, 0)
        break

for s in ret:
  for ss in s:
    print(ss, end=' ')
  print()