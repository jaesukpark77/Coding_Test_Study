# problem link : https://www.codetree.ai/missions/8/problems/longest-round-trip?&utm_source=clipboard&utm_medium=text

import math

INT_MAX = math.inf

n, m, x = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(m)]

graph1 = [[0] * (n + 1) for _ in range(n + 1)]
graph2 = [[0] * (n + 1) for _ in range(n + 1)]

dist1 = [INT_MAX] * (n + 1)
dist2 = [INT_MAX] * (n + 1)

ans = 0

def dijkstra(dist, graph):
    visited = [False] * (n + 1)

    dist[x] = 0

    for i in range(1, n+1):
        min_index = -1
        for j in range(1, n+1):
            if visited[j]:
                continue

            if min_index == -1 or dist[min_index] > dist[j]:
                min_index = j
        
        visited[min_index] = True

        for j in range(1, n+1):
            if graph[min_index][j] == 0:
                continue
            
            dist[j] = min(dist[j], dist[min_index] + graph[min_index][j])

for a, b, c in edges:
    graph1[a][b] = c

dijkstra(dist1, graph1)

for a, b, c in edges:
    graph2[b][a] = c

dijkstra(dist2, graph2)

for i in range(1, n + 1):
    ans = max(ans, dist1[i] + dist2[i])

print(ans)