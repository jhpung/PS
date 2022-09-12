# 예시 문제는 백준의 최단경로 문제이다.
# (https://www.acmicpc.net/problem/1753)

from heapq import heappop, heappush
import sys

input = sys.stdin.readline

# 정점과 간선의 갯수 할당
node_n, edge_n = map(int, input().split())

# 시작하는 정점 할당
start = int(sys.stdin.readline())

# 그래프 변수 선언
graph = [[] for i in range(node_n + 1)]

# 최단 거리 변수 선언
result = [sys.maxsize for _ in range(node_n + 1)]

for _ in range(edge_n):
    origin, dest, weight \
        = map(int, input().split())

    # 그래프 간선 정보 초기화
    heappush(graph[origin], (weight, dest))

heap_queue = []

result[start] = 0
heappush(heap_queue, (0, start))

while heap_queue:
    # 큐가 빌 때까지 반복한다.
    # 큐가 비면 알고리즘 종료.
    weight, node = heappop(heap_queue)

    # 현재 가중치보다 최단 거리 테이블에 기록된
    # 가중치가 더 낮다면, continue
    if result[node] < weight:
        continue

    # 현재 큐에서 가져온 노드와 연결된 모든 노드를 탐색한다.
    while graph[node]:
        next_weight, next_node = heappop(graph[node])

        # 현재 큐에서 가져온 노드 N1
        # N1과 연결된 노드 N2

        # 시작 지점에서 N1까지의 최단거리와
        # N1에서 N2로 가는 거리르 더한다
        cost = weight + next_weight

        # 그 값이 최단 거리 테이블에 이미 기록된 값보다 작으면
        # 최단거리 테이블을 업데이트한다.
        if cost < result[next_node]:
            result[next_node] = cost
            heappush(heap_queue, (cost, next_node))

for node in range(1, node_n + 1):
    if result[node] == sys.maxsize:
        print("INF")
    else:
        print(result[node])
