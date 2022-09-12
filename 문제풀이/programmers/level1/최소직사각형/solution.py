

def solution(sizes: list):
    result = 0
    maxHeight = None
    maxWidth = None

    for i in range(0, len(sizes)):
        [height, width] = sizes[i]

        if height > width:
            temp = width
            width = height
            height = temp


        if i == 0:
            maxHeight = height
            maxWidth = width
            continue

        if maxHeight < height:
            maxHeight = height

        if maxWidth < width:
            maxWidth = width

    print(maxHeight, maxWidth)
    return maxHeight * maxWidth


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
