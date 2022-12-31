from collections import defaultdict
import operator

N, C = map(int, input().split())

dd = defaultdict(int)

cur = list(map(int,input().split()))

for num in cur:
  dd[num] += 1

list = sorted(dd.items(), key=operator.itemgetter(1), reverse=True)

for (k, v) in list:
  for i in range(v):
    print(k, end=" ")

