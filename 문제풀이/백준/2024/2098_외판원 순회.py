import sys
input = sys.stdin.readline

MAX_VALUE = 1_000_001 * 16
N = int(input())
ALL_VISITED = pow(2, N) - 1
graph = []
dp = [[0 for _ in range(ALL_VISITED)] for _ in range(N) ]

for _ in range(N):
    graph.append(list(map(int, input().split())))

def node_bit(node:int):
    return 1 << node

def tsp(curr: int, visited: int):
    global N, ALL_VISITED, MAX_VALUE, graph
    
    if visited == ALL_VISITED:
        return graph[curr][0] if graph[curr][0] != 0 else MAX_VALUE
    
    if dp[curr][visited] != 0:
        return dp[curr][visited]
    
    dp[curr][visited] = MAX_VALUE
    
    for next in range(N):
        next_visited = visited | node_bit(next)
    
        if graph[curr][next] != 0 and (visited & node_bit(next)) == 0:
            dp[curr][visited] = min(dp[curr][visited], tsp(next, next_visited) + graph[curr][next])
    
    return dp[curr][visited]

result= (tsp(0, 1))

print(result)