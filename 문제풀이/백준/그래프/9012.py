import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
  s = input()

  st = []
  good = True

  for ch in s.strip():
    if ch == '(':
      st.append(ch)
      continue

    if not len(st):
      good = False
      break

    if ch == ')' and st[-1] == '(':
      st.pop()
      continue
  if st:
    good = False
  if good: 
    print("YES")
  else:
    print("NO")

