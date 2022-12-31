N = int(input())

ret = []

for i in range(N):
  s = input()

  tmp = ''
  for j in range(len(s)):
    c = s[j]

    is_numeric = c.isnumeric()

    if not is_numeric:
      if len(tmp):
        ret.append(int(tmp))  
      tmp = ''
      continue

    is_zero = c == '0'

    if is_numeric and is_zero and tmp == '0':
      continue

    if is_numeric:
      tmp += c
  
  if len(tmp):
    ret.append(int(tmp))

ret.sort()

for i in (ret):
  print(i)


    
    

