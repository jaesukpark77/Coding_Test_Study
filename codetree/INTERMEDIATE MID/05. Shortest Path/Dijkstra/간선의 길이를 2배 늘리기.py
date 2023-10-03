# problem link : https://www.codetree.ai/missions/8/problems/double-the-length-of-the-edge?&utm_source=clipboard&utm_medium=text

import math

INT_MAX = math.inf

n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
dist = [0] * (n + 1)
path = [0] * (n + 1)

ans = 0

for _ in range(m):
    x, y, z = tuple(map(int, input().split()))
    graph[x][y] = z
    graph[y][x] = z

def dijkstra():
    for i in range(1, n+1):
        dist[i] = INT_MAX

    dist[1] = 0

    for i in range(1, n + 1):
        visited[i] = False

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
            
            if dist[j] > dist[min_index] + graph[min_index][j]:
                dist[j] = dist[min_index] + graph[min_index][j]
                path[j] = min_index

dijkstra()

x = n
vertices = []
vertices.append(x)

while x!= 1:
    x = path[x]
    vertices.append(x)

orig_dist = dist[n]

length = len(vertices)
for i in range(length - 1, 0, -1):
    x = vertices[i]
    y = vertices[i - 1]
    graph[x][y] *= 2
    graph[y][x] *= 2

    dijkstra()

    ans = max(ans, dist[n] - orig_dist)

    graph[x][y] //= 2
    graph[y][x] //= 2

print(ans)