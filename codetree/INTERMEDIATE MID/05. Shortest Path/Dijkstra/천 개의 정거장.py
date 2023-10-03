# problem link : https://www.codetree.ai/missions/8/problems/thousand-stops?&utm_source=clipboard&utm_medium=text

import math

INF = math.inf

m = 1000

a, b, n = map(int, input().split())
graph = [[(INF, 0)] * (m + 1) for _ in range(m + 1)]
dist = [(INF, 0)] * (m + 1)
visited = [False] * (m + 1)

for i in range(1, m+1):
    graph[i][i] = (0, 0)

for _ in range(n):
    cost, stop_num = tuple(map(int, input().split()))
    stops = list(map(int, input().split()))

    for i in range(stop_num):
        for j in range(i+1, stop_num):
            graph[stops[i]][stops[j]] = min(graph[stops[i]][stops[j]], (cost, j - i))

dist[a] = (0, 0)

for _ in range(m):
    min_index = -1
    for i in range(1, m + 1):
        if visited[i]:
            continue
        
        if min_index == -1 or dist[min_index] > dist[i]:
            min_index = i

    visited[min_index] = True
    min_cost, min_time = dist[min_index]

    for i in range(1, m + 1):
        cost, time = graph[min_index][i]
        dist[i] = min(dist[i], (min_cost + cost, min_time + time))

if dist[b] == (INF, 0):
    dist[b] = (-1, -1)

min_cost, min_time = dist[b]

print(min_cost, min_time)