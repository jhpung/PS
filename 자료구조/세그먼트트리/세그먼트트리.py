import math
import sys

# 예제 문제는 https://www.acmicpc.net/problem/2042 이다.
input = sys.stdin.readline

n, m, k = map(int, input().split())

tree = [None for i in range(n + 1)]
segment_tree = [None for i in range(n * 4)]


def init(start: int, end: int, node: int):
    global tree
    global segment_tree

    if start == end:
        segment_tree[node] = tree[start]

        return segment_tree[node]

    mid = ((start + end) // 2)

    segment_tree[node] = init(start, mid, node * 2) + \
        init(mid + 1, end, node * 2 + 1)

    return segment_tree[node]


def sum(start: int, end: int, node: int, left: int, right: int):
    global segment_tree

    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return segment_tree[node]

    mid = ((start + end) // 2)

    return sum(start, mid, node * 2, left, right) + sum(mid + 1, end, node * 2 + 1, left, right)


def update(start: int, end: int, node: int, index: int, diff: int):
    global segment_tree

    if start > index or end < index:
        # 범위 밖이면 업데이트 안해도 된다.
        return

    segment_tree[node] = segment_tree[node] + diff

    mid = ((start + end) // 2)

    if start == end:
        # 이 문제에서는 diff를 여러번 계산하기 때문에 원본트리도 갱신해줘야 한다.
        tree[start] = tree[start] + diff
    if start != end:
        # 리프 노드가 아니라면 재귀
        update(start, mid, node * 2, index, diff)
        update(mid + 1, end, node * 2 + 1, index, diff)


for i in range(1, n + 1):
    num = int(input())

    tree[i] = num

init(1, n, 1)
for i in range(m + k):
    a, b, c = map(int, input().split())

    if a == 1:
        index = b
        diff = c - tree[b]
        update(1, n, 1, index, diff)
        continue

    if a == 2:
        left = b
        right = c
        print(sum(1, n, 1, left, right))
