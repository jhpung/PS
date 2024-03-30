from collections import defaultdict
import heapq

def solution(n, ts):
    answer = 0
    curr = 0
    
    heap = []
    counter = defaultdict(int)
    
    for t in ts:
        counter[t] += 1
        
    for k, v in counter.items():
        heapq.heappush(heap, (-v, k))
    
    print(heap)
    while curr < n:
        answer += 1
        v, k = heapq.heappop(heap)
        real = -v
        
        curr += real
    return answer