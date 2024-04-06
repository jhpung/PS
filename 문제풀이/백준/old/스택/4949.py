import sys
input = sys.stdin.readline


while True:
  flag = True
  s = input().replace('\n', '')

  if s == '.':
    break

  st = []

  for ch in s:
    if ch == '(':
      st.append(ch)
    elif ch == '[':
      st.append(ch)
    elif ch == ')':
      if not st or st[-1] != '(':
        flag = False
        break
      st.pop()
    elif ch == ']':
      if not st or st[-1] != '[':
        flag = False
        break
      st.pop()
  
  if st:
    flag = False
  
  if flag:
    print('yes')
  else:
    print('no')
