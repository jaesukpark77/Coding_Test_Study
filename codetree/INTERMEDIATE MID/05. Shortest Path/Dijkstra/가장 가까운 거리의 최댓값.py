# problem link : https://www.codetree.ai/missions/8/problems/maximum-of-nearest-distance?&utm_source=clipboard&utm_medium=text

import heapq
import math

INT_MAX = math.inf
INT_MIN = -math.inf

n, m = map(int, input().split())
a, b, c = map(int,input().split())

graph = [[] for _ in range(n + 1)]
pq = []

abc_dist = [INT_MAX] * (n + 1)
ans = INT_MIN

for _ in range(m):
    x, y, z = tuple(map(int, input().split()))
    graph[x].append((y, z))
    graph[y].append((x, z))

def dijkstra(k):
    dist = [INT_MAX] * (n + 1)

    dist[k] = 0
    
    heapq.heappush(pq, (0, k))

    while pq:
        min_dist, min_index = heapq.heappop(pq)
        
        if min_dist != dist[min_index]:
            continue

        for target_index, target_dist in graph[min_index]:
            new_dist = dist[min_index] + target_dist
            if dist[target_index] > new_dist:
                dist[target_index] = new_dist
                heapq.heappush(pq, (new_dist, target_index))

    for i in range(1, n + 1):
        abc_dist[i] = min(abc_dist[i], dist[i])

dijkstra(a)
dijkstra(b)
dijkstra(c)

for i in range(1, n+1):
    ans = max(ans, abc_dist[i])

print(ans)