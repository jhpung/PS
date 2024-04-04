from collections import defaultdict
n, m = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()

dp = defaultdict(bool)

def sol(arr, start, depth):
    curr = arr[0:depth]
    key = "-".join(map(str, curr))
    if depth == m and not dp[key]:
        dp[key] = True
        print(' '.join(map(str, curr)))
    elif dp[key]:
        return
    else:
        for i in range(start, n):
            if arr and arr[-1] > lst[i]:
                continue
            else:
                arr.append(lst[i])
                sol(arr, 0, depth + 1)
                arr.pop()


sol([], 0, 0)