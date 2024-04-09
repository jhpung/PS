import sys
from collections import defaultdict
class Dir:
    LEFT = 0
    RIGHT = 1
    
N, S = map(int, input().split())

a = list(map(int, input().split()))

mid = N // 2
ret = 0

ldict = defaultdict(int)
rdict = defaultdict(int)

def left(pos: int, sum: int):
    if pos == mid:
        ldict[sum] += 1
        return
    
    # a[pos] 원소를 추가한 부분 수열
    left(pos + 1, sum + a[pos])

    # a[pos] 원소를 미추가한 부분 수열
    left(pos + 1, sum)

def right(pos: int, sum: int):
    global ret
    if pos == N:
        ret += ldict[S - sum]
        return
    
    right(pos + 1, sum + a[pos])
    right(pos + 1, sum)
    
left(0, 0)
right(mid, 0)

if S  == 0:
    print(ret - 1)
else:
    print(ret)