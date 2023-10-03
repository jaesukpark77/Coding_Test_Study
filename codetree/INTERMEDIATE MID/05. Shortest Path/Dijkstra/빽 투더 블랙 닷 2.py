# problem link : https://www.codetree.ai/missions/8/problems/back-to-the-black-dot-2?&utm_source=clipboard&utm_medium=text

import math
import heapq

INT_MAX = math.inf
n, m = map(int, input().split())
a, b = map(int, input().split())

graph = [[] for _ in range(n + 1)]
pq = []

red_dist1 = [INT_MAX] * (n + 1)
red_dist2 = [INT_MAX] * (n + 1)

ans = INT_MAX

for _ in range(m):
    x, y, z = tuple(map(int, input().split()))
    graph[x].append((y, z))
    graph[y].append((x, z))

def dijkstra(k, dist):
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

dijkstra(a, red_dist1)
dijkstra(b, red_dist2)

for i in range(1, n+1):
    if i == a or i == b:
        continue

    ans = min(ans, red_dist1[i] + red_dist1[b] + red_dist2[i])

    ans = min(ans, red_dist2[i] + red_dist2[a] + red_dist1[i])

if ans == INT_MAX:
    ans = -1

print(ans)