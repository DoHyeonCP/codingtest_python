import sys
from collections import deque


def isBipartite(graph, start, color):
    queue = deque([start])
    color[start] = 1

    while queue: #
        v = queue.popleft()
        for i in graph[v]:
            if color[i] == 0:
                color[i] = -color[v]
                queue.append(i)
            elif color[i] == color[v]:
                return False
    return True

input = sys.stdin.readline
K = int(input())
for _ in range(K):
    V, E = map(int, input().split()) # 그래프의 정점의 수와 간선의 수를 입력 받는다.
    graph = [[] for _ in range(V + 1)]
    color = [0] * (V + 1)

    for _ in range(E): # 간선의 수만큼 반복하여 연결된 정점의 관계를 표현한다.
        u, v = map(int, input().split()) 
        graph[u].append(v)
        graph[v].append(u)

    bipartite = True
    for v in range(1, V + 1): # 
        if color[v] == 0:
            if not isBipartite(graph, v, color):
                bipartite = False
                break

    print("YES" if bipartite else "NO")