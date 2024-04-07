from collections import deque, defaultdict
import sys
input = sys.stdin.readline

EMPTY = '.'
WALL = '#'
GOAL = 'O'
RED = 'R'
BLUE = 'B'

TILT_LEFT = 0
TILT_TOP = 1
TILT_RIGHT = 2
TILT_BOTTOM = 3

TILT_DIRS = [(0, -1), (-1, 0), (0, 1), (1, 0)]

R, C = map(int, input().split())

mp = []

rpos = None
bpos = None

for h in range(R):
    mp.append(input().strip())
    
    rindex =  mp[h].find(RED)
    if rindex != -1:
        rpos = (h, rindex)
    bindex =  mp[h].find(BLUE)
    if bindex != -1:
        bpos = (h, bindex)

visited = defaultdict(bool)

queue = deque([(0, rpos, bpos)])

def tilt(dir, y, x):
    while True:
        dy, dx = TILT_DIRS[dir]
        ny, nx = y + dy, x + dx
    
        if ny < 0 or ny >= R or nx < 0 or nx >= C:
            return (y, x)
        if mp[ny][nx] == WALL:
            return (y, x)
        if mp[ny][nx] == GOAL:
            return (ny, nx)
        
        y, x = ny, nx
        
result = -1

while queue and result == -1:
    count, rpos, bpos = queue.popleft()
    ry, rx = rpos
    by, bx = bpos
    key = f"{ry}-{rx}-{by}-{bx}"
    ncount = count + 1
    
    if visited[key]:
        continue
    
    visited[key] = True
    
    for dir in [TILT_LEFT, TILT_TOP, TILT_RIGHT, TILT_BOTTOM]:
        nby, nbx = tilt(dir, by, bx)
        nry, nrx = tilt(dir, ry, rx)
        
        if mp[nby][nbx] == GOAL: 
            continue

        if (nby, nbx) == (nry, nrx):
            if dir == TILT_LEFT:
                if rx < bx:
                    nbx = nrx + 1
                else:
                    nrx = nbx + 1
            if dir == TILT_RIGHT:
                if rx > bx:
                    nbx = nrx - 1
                else:
                    nrx = nbx - 1
            if dir == TILT_TOP:
                if ry > by:
                    nry = nby + 1
                else:
                    nby = nry + 1
            if dir == TILT_BOTTOM:
                if ry < by:
                    nry = nby - 1
                else:
                    nby = nry - 1
        nkey = f"{nry}-{nrx}-{nby}-{nbx}"
        if visited[nkey]:
            continue

        if mp[nry][nrx] == GOAL:
            result = ncount
            break
        
        if ncount == 10:
            continue
                
        queue.append((ncount, (nry, nrx), (nby, nbx)))
        
print(result)