# problem link : https://www.codetree.ai/missions/8/problems/longest-student-2?&utm_source=clipboard&utm_medium=text

import heapq
import math

INT_MAX = math.inf

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
pq = []

dist = [INT_MAX] * (n + 1)

for _ in range(m):
    x, y, z = tuple(map(int, input().split()))
    graph[y].append((x, z))

dist[n] = 0

heapq.heappush(pq, (0, n))

while pq:
    min_dist, min_index = heapq.heappop(pq)

    if min_dist != dist[min_index]:
        continue
    
    for target_index, target_dist in graph[min_index]:
        new_dist = dist[min_index] + target_dist

        if dist[target_index] > new_dist:
            dist[target_index] = new_dist
            heapq.heappush(pq, (new_dist, target_index))

ans = 0

for i in range(1, n):
    ans = max(ans, dist[i])

print(ans)