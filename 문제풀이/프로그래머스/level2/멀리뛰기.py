def solution(n = 0):
    dp = [1, 2] + [None for i in range(n - 2)]

    if n <= 2:
        return dp[n - 1]

    for i in range(2, n):
        dp[i] = (dp[i-1] + dp[i-2])
    
    return dp[n - 1] % 1234567