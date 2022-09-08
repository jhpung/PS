

dirs = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
]


def solution(maps: list):
    queue = [[0, 0, 1]]

    height = len(maps)
    width = len(maps[0])

    visited = [[False for x in range(width)] for y in range(height)]

    while queue:
        x, y, count = queue.pop(0)

        if visited[y][x]:
            continue
        
        visited[y][x] = True

        if x == width - 1 and y == height - 1:
            return count

        for dir in dirs:
            nx, ny = x + dir[0], y + dir[1]

            if nx < 0 or nx >= width or ny < 0 or ny >= height:
                continue
            if visited[ny][nx]:
                continue
            if not maps[ny][nx]:
                continue

            queue.append([nx, ny, count + 1])
    return -1


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
    1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
