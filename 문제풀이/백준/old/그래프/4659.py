
while True:
  c = input()
  
  if c == 'end': break

  mo = ['a', 'e', 'i','o','u']

  mo_exists = False
  last = None
  mo_count = 0
  ja_count = 0
  good = True
  for i in range(len(c)):
    curr = c[i]
    

    if curr not in ['e', 'o'] and curr == last:
      print('<{}> is not acceptable.'.format(c))
      good = False
      break
    last = curr

    if curr in mo:
      mo_exists = True
      mo_count += 1
      ja_count = 0
    else:
      mo_count = 0
      ja_count += 1

    if ja_count >= 3 or mo_count >= 3:
      print('<{}> is not acceptable.'.format(c))
      good = False
      break

  if not good:
    continue
    
  if not mo_exists:
    print('<{}> is not acceptable.'.format(c))
    continue
  
  print('<{}> is acceptable.'.format(c))

