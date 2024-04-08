import sys

input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 2)
nums = list(map(int, input().split()))

curr = []

def search(arr: list, start: int, end: int, value: int):
    if start >= end:
        return start
    
    mid = (start + end) // 2
    
    if arr[mid] > value:
        return search(arr, start, mid, value)
    elif arr[mid] == value:
        return mid
    else:
        return search(arr, mid + 1, end, value)
    

for num in nums:
    if not curr:
        curr.append(num)
        continue
    
    if curr[-1] < num:
        curr.append(num)
        continue
    
    index = search(curr, 0, len(curr) - 1, num)
    
    curr[index] = num
    
print(len(curr))