from collections import deque

N, S = map(int, input().split())

nums = list(map(int, input().split()))
sums = [0]

for n in nums:
    sums.append(sums[-1] + n)
        
# 현재 수열의 합이 S 이상이면 start를 플러스한다.
# 현재 수열의 합이 S 이하이면 end를 플러스한다.
# 이를 end가 N이 되기 전까지 반복한다.

start = 0
end = 1
mLine = 100_001

while end <= N:
    if sums[end] - sums[start] < S:
        end += 1
    else:
        mLine = min(end - start, mLine)
        start += 1

if mLine == 100_001:
    print(0)
else:
    print(mLine)