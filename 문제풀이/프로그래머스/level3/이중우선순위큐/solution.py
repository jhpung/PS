from collections import defaultdict
from queue import PriorityQueue
import sys

# 우선순위 큐 두개를 써서 풀 수 있다.
# 근데, 굳이 우선순위 큐 안써도 다른사람들은 잘 푼 듯...
# 프로그래머스에서 자체적으로 달아 놓은 카테고리를
# 벗어나서 해답을 찾는 것도 나을 것 같다.

def solution(operations: list):
    answer = []

    maxQ = PriorityQueue()
    minQ = PriorityQueue()
    map = defaultdict(int)

    for operation in operations:
        op, valueStr = operation.split(' ')
        value = int(valueStr)

        print(map)
        if op == 'I':
            maxQ.put(-value)
            minQ.put(value)
            map[value] = map[value] + 1

        elif op == 'D':
            if value == 1:
                while not maxQ.empty():
                    max = -1 * maxQ.get()

                    if map[max]:
                        map[max] = map[max] - 1
                        break

            elif value == -1:
                while not minQ.empty():
                    min = (minQ.get())
                    print(min)

                    if map[min]:
                        map[min] = map[min] - 1
                        break

    empty = True
    for key, value in map.items():
        if value:
            empty = False
            break

    if empty:
        return [0, 0]

    max = 0
    min = sys.maxsize
    for key in map.keys():
        if map[key] and key > max:
            max = key

        if map[key] and key < min:
            min = key

    print(map)
    return [max, min]


solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
