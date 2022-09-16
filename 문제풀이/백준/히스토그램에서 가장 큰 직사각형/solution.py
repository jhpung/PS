import sys


input = sys.stdin.readline

# 구간 합인데 조건을 달아야 한다.
# 직사각형이라면, 현재 노드가, 왼쪽 노드와 높이가 같거나 더 커야 한다.
# 이런 경우의 구간합을 구하면 된다.

nums = [None for _ in range(100_000)]
tree = [None for _ in range(400_000)]
maximum = None


def init(start: int, end: int, node: int):
    if start == end:
        tree[node] = (nums[start], 1)
        return tree[node]

    mid = (start + end) // 2

    left_height, left_width = init(start, mid, node * 2)
    right_height, right_width = init(mid + 1, end, node * 2 + 1)

    result = None
    if left_height < right_height:
        merged_left = (left_height) * (left_width + right_width)
        merged_right = (right_height) * (right_width)

        if merged_left < merged_right:
            result = (right_height, right_width)

        if merged_left > merged_right:
            result = (left_height, left_width + right_width)

        if merged_left == merged_right:
            result = (right_height, right_width)

    if left_height > right_height:
        merged_right = (right_height) * (right_width + left_width)
        merged_left = (left_height) * (left_width)

        if merged_left < merged_right:
            result = (right_height, right_width + left_width)
        if merged_left > merged_right:
            result = (left_height, left_width)
        if merged_left == merged_right:
            result = (left_height, left_width)

    if left_height == right_height:
        result = ((left_height), (left_width + right_width))

    tree[node] = result

    return tree[node]


while True:
    l = list(map(int, input().split()))

    n = l[0]

    if n == 0:
        break

    for i in range(1, n + 1):
        nums[i] = l[i]

    init(1, n, 1)

    print(tree)
    height, width = tree[1]

    print(height * width)
