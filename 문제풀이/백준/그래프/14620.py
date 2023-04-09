import sys
input = sys.stdin.readline

N = int(input())

dirs = [(0,0),(1,0), (0,1), (-1,0), (0, -1) ]
ret = sys.maxsize

mp = []
visited = [[False for _ in range(12)] for _ in range(12)]


def check(y,x):
    global visited, dirs, mp
    sum = 0

    for dy,dx in dirs:
        ny,nx = y + dy, x + dx

        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            return -1
        if visited[ny][nx]:
            return -1
        sum += mp[ny][nx]

    return sum
    
def mark(y,x):
    global visited, dirs
    for dy,dx in dirs:
        ny,nx = y + dy, x + dx

        visited[ny][nx] = True

def unmark(y,x):
    global visited, dirs
    for dy,dx in dirs:
        ny,nx = y + dy, x + dx

        visited[ny][nx] = False
    
def go(idx, sum):
    global ret
    if idx == 3:
        ret = min(ret, sum)
        return
    if sum > ret:
        return
    for i in range(1, N-1):
        for j in range(1, N-1):
            result = check(i,j)

            if result >= 0 and sum + result < ret:
                mark(i,j)
                go(idx + 1, sum + result)
                unmark(i,j)
                
for i in range(N):
    mp.append(list(map(int, input().split())))


go(0, 0)

print(ret)


