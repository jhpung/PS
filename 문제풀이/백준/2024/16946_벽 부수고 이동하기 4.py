import sys
from collections import deque, defaultdict
input = sys.stdin.readline

H, W = map(int, input().split())

EMPTY, WALL = '0', '1'

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

MP = []


for _ in range(H):
    MP.append(list(input()))

RESULT = [['0' for _ in range(W)] for _ in range(H)]
group = [[None for _ in range(W)] for _ in range(H)]
group_num = 0
group_count = defaultdict(int)

wall_queue = deque()

for i in range(H):
    for j in range(W):
        if MP[i][j] == WALL:
            wall_queue.append((i,j))
            continue
        if group[i][j] is not None:
            continue
        
        group_num += 1
        queue = deque()
        queue.append((i, j))
        group[i][j] = group_num
        cnt = 1
        while queue:
            cy, cx = queue.popleft()
            for dy, dx in DIRS:
                ny, nx = cy + dy, cx + dx
                
                if ny < 0 or ny >= H or nx < 0 or nx >= W:
                    continue
                
                if MP[ny][nx] == WALL:
                    continue
                
                if group[ny][nx] is not None:
                    continue
                
                group[ny][nx] = group_num
                queue.append((ny, nx))
                cnt += 1
        
        group_count[group_num] = cnt
    
while wall_queue:
    cy, cx = wall_queue.popleft()
    
    cnt = 1
    checked = defaultdict(bool)
    
    for dy, dx in DIRS:
        ny, nx = cy + dy, cx + dx

        if ny < 0 or ny >= H or nx < 0 or nx >= W:
            continue
        
        if MP[ny][nx] == WALL:
            continue
        
        group_num = group[ny][nx]
        
        if checked[group_num]:
            continue
        
        checked[group_num] = True
        cnt += group_count[group_num]
        
    RESULT[cy][cx] = str(cnt % 10)

for line in RESULT:
    print("".join(line))