# 테두리의 갯수는 테두리 안 도형의
# 넓이 * 2 + 높이 * 2 + 4 다.
# 이를 이용해서 높이 1부터 1씩 높여가며
# brown과 일치하는지 매번 확인하면 끝

import math


def solution(brown, yellow):
    maxHeight = math.ceil(math.sqrt(yellow))

    for height in range(1, maxHeight + 1):
        width = yellow / height

        print(brown)
        print(height, width)
        if (height * 2 + width * 2 + 4) == brown:
            return [width + 2, height + 2]
