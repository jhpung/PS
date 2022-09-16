# DP로 풀었지만 만족스럽진 않다. 다음에 더 좋은 풀이를 고민해봐야 할 듯.
# 1. 각 자리의 최대 누적값을 DP로 처리한다.
# 2. 밑에서는 왼쪽 대각선 위와 오른쪽 대각선 위의 최대 누적값 중, 큰 수와 더해 자신의 누적값을 저장한다.
# 3. 위 과정을 맨 밑 라인까지 진행한 후, 마지막 라인의 최대 값을 뽑아서 리턴하면 완료
def solution(triangle: list):
    dp = []

    for i in range(len(triangle)):
        dp.append([None for _ in range(i + 1)])

    dp[0][0] = triangle[0][0]
    dp[1][0] = dp[0][0] + triangle[1][0]
    dp[1][1] = dp[0][0] + triangle[1][1]

    for i in range(2, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
                continue
            elif j == len(triangle[i]) - 1:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                continue

            upperLeftIndex = j - 1
            upperRightIndex = j
            upperLeftAcc = dp[i-1][upperLeftIndex]
            upperRightAcc = dp[i-1][upperRightIndex]

            dp[i][j] = upperLeftAcc + \
                triangle[i][j] if upperLeftAcc > upperRightAcc else upperRightAcc + triangle[i][j]

    result = 0

    for j in range(len(dp[-1])):
        curr = dp[-1][j]
        if result < curr:
            result = curr

    return result


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
