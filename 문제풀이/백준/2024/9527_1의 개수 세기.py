import sys

A, B = map(int, input().split())
DP = []

DP.append(1)
for i in range(1, 55):
    DP.append(DP[i - 1] * 2 + pow(2, i))
    
def get(n: int):
    ans = n & 1
    for i in range(0, 55):
        curr = 55 - i
        if n & (1 << curr):
            ans += DP[curr - 1]
            ans += n - (1 << curr) + 1
            n = n - (1 << curr)
    return ans

print(get(B) - get(A - 1))