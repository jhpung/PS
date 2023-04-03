from functools import reduce
from heapq import heapify, heappush, heappop, heapreplace

# 힙을 사용해 O(NlogN)의 시간복잡도로 해결할 수 있다.


def solution(n=int, works=list):
    answer = 0

    minimum = min(works)

    heap = []

    # heapify O(NlogN)
    for i in works:
        heappush(heap, (-i, i))

    # O(NlogN)
    for i in range(n):
        key, value = heappop(heap)

        value = value - 1 if value - 1 >= 0 else 0
        key = key + 1 if key + 1 <= 0 else 0

        heappush(heap, (key, value))

    # O(N)
    for i in heap:
        answer += i[1] ** 2

    return answer
