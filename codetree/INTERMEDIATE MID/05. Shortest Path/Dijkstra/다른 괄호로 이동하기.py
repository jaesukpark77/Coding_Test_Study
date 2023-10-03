# problem link : https://www.codetree.ai/missions/8/problems/move-to-another-parenthesis?&utm_source=clipboard&utm_medium=text

import heapq
import math

INT_MAX = math.inf
MAX_M = 900

n, a, b = map(int, input().split())
brackets = [[" "] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    brackets[i] = " " + input()

m = 0
node_num = [[0] * (n + 1) for _ in range(n + 1)]
graph = [[] for _ in range(MAX_M + 1)]
pq = []

dist = [0] * (MAX_M + 1)
ans = 0

def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

def make_graph():
    global m

    for i in range(1, n+1):
        for j in range(1, n+1):
            m += 1
            node_num[i][j] = m

    for x in range(1, n+1):
        for y in range(1, n+1):
            dxs, dys = [-1, 1, 0, 0], [0, 0, 1, -1]

            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny):
                    node1 = node_num[x][y]
                    node2 = node_num[nx][ny]

                    cost = a if brackets[x][y] == brackets[nx][ny] else b
                    graph[node1].append((node2,  cost))

def dijkstra(k):
    for i in range(1, m + 1):
        dist[i] = INT_MAX

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

make_graph()

for i in range(1, m+1):
    dijkstra(i)

    for j in range(1, m+1):
        ans = max(ans, dist[j])

print(ans)