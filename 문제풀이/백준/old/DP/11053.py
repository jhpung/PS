import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 2)
nums = list(map(int, input().split()))
cnt = [0] * 100000
last = 0
ret = 0
for i in range(len(nums)):
    maxValue = 0
    for j in range(i):
        if nums[j] < nums[i] and maxValue < dp[j]:
            maxValue = dp[j]
    dp[i] = maxValue + 1
    ret = max(ret, dp[i])


print(ret)
