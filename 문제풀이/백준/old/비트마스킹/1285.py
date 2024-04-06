import sys
input = sys.stdin.readline
N = int(input())
a = [0 for _ in range(44)]
ret = sys.maxsize


def go(here=int):
    global ret
    if here == N + 1:
        sum = 0
        i = 1
        while i <= (1 << (N-1)):
            cnt = 0
            for j in range(1, N + 1):
                # 동전이 앞면이라면
                if a[j] & i:
                    cnt += 1
            sum += min(cnt, N - cnt)
            i *= 2
        ret = min(ret, sum)
        return

    go(here + 1)
    a[here] = ~a[here]
    go(here + 1)


for i in range(1, N + 1):
    s = input()
    value = 1
    for j in range(len(s)):
        if s[j] == 'T':
            a[i] |= value
        value *= 2
go(1)
print(ret)
