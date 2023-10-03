# problem link : https://www.codetree.ai/missions/8/problems/shortest-path-to-each-vertex-2?&utm_source=clipboard&utm_medium=text

import math

INT_MAX = math.inf

n, m = map(int, input().split())

dist = [[INT_MAX] * (n + 1) for _ in range(n + 1)]

for i in range(1, n+1):
    dist[i][i] = 0

for _ in range(m):
    x, y, z = tuple(map(int, input().split()))
    dist[x][y] = min(dist[x][y], z)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] == INT_MAX:
            print(-1, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()