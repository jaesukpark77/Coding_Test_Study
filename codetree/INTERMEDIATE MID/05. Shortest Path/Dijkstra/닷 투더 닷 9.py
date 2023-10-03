# problem link : https://www.codetree.ai/missions/8/problems/dot-to-the-dot?&utm_source=clipboard&utm_medium=text

import heapq
import math

INT_MAX = math.inf

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
pq = []

c_list = []
dist = [0] * (n + 1)

ans = INT_MAX

for _ in range(m):
    a, b, l, c = tuple(map(int, input().split()))
    graph[a].append((b, l, c))
    graph[b].append((a, l, c))

    c_list.append(c)

def dijkstra(k, c_limit):
    for i in range(1, n+1):
        dist[i] = INT_MAX

    dist[k] = 0

    heapq.heappush(pq, (0, k))
    
    while pq:
        min_dist, min_index = heapq.heappop(pq)

        if min_dist != dist[min_index]:
            continue

        for target_index, target_l, traget_c in graph[min_index]:
            if traget_c < c_limit:
                continue

            new_dist = dist[min_index] + target_l
            if dist[target_index] > new_dist:
                dist[target_index] = new_dist

                heapq.heappush(pq, (new_dist, target_index))

for c_limit in c_list:
    dijkstra(1, c_limit)

    ans = min(ans, dist[n] + x / c_limit)

print(int(ans))