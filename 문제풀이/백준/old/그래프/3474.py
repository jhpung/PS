import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
  C = int(input())

  ret2 = 0
  ret5 = 0
  j = 2
  while j <= C:
    ret2 += C // j
    j *= 2

  j = 5

  while j <= C:
    ret5 += C // j
    j *= 5

  print(min(ret2, ret5)) 

