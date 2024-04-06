import sys

input = sys.stdin.readline
N, K = map(int, input().split())

words = [0] * 51


def count(mask: int):
    cnt = 0
    for word in words:
        if word and word & mask == word:
            cnt += 1

    return cnt


def go(index: int, k: int, mask: int):
    if k < 0:
        return 0
    if index == 26:
        return count(mask)

    ret = go(index + 1, k - 1, mask | (1 << index))

    if index != ord('a') - ord('a') and index != ord('n') - ord('a') and index != ord('t') - ord('a') and index != ord('i') - ord('a') and index != ord('c')-ord('a'):
        ret = max(ret, go(index + 1, k, mask))

    return ret


for i in range(N):
    s = input().strip()

    for c in s:
        words[i] |= (1 << (ord(c) - ord('a')))

print(go(0, K, 0))
