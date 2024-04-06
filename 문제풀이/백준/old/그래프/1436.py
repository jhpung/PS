import sys
input = sys.stdin.readline

N = int(input())

count = 0
curr = 666

  

while True:
  s = str(curr)

  if s.find('666') != -1:
    count += 1
  
  if count == N:
    break 
  
  curr += 1

print(curr)
