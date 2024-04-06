from collections import deque, defaultdict

N = int(input())

lst = list(map(int, input().split()))
tree = defaultdict(set)

for node, parent in enumerate(lst):
    tree[parent].add(node)

target = int(input())


for key in tree.keys():
    if target in tree[key]:
        tree[key].remove(target)
        break
q = deque()
q.append(-1)

answer = 0
while q:
    curr = q.popleft()
    if not tree[curr]:
        if curr == -1:
            break
        answer += 1
    else:
        q.extend(tree[curr])
print(answer)
