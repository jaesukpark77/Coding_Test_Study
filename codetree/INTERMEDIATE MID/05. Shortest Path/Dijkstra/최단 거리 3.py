# problem link : https://www.codetree.ai/missions/8/problems/shortest-distance-3?&utm_source=clipboard&utm_medium=text

import math

INT_MAX = math.inf

n, m = map(int, input().split())
graph = [[INT_MAX] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n+1)

dist = [INT_MAX] * (n + 1)

for _ in range(m):
    x, y, z = tuple(map(int, input().split()))
    graph[x][y] = min(graph[x][y], z)
    graph[y][x] = min(graph[y][x], z)
    
a, b = tuple(map(int, input().split()))

dist[a] = 0

for i in range(1, n + 1):
    min_index = -1
    for j in range(1, n+1):
        if visited[j]:
            continue
        
        if min_index == -1 or dist[min_index] > dist[j]:
            min_index = j

    visited[min_index] = True

    for j in range(1, n+1):
        dist[j] = min(dist[j], dist[min_index] + graph[min_index][j])

print(dist[b])