import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
st = [(0, nums[0])]
result = [-1 for _ in range(N)]

for i in range(1, N):
  if not st:
    st.append((i, nums[i]))
    continue
  
  while st:
    top = st[-1]
    pos, val = top

    if val < nums[i]:
      result[pos] = nums[i]
      st.pop()
    else:
      break
  
  st.append((i, nums[i]))

for i in result:
  print(i, end=" ")


