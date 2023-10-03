# problem link : https://www.codetree.ai/missions/8/problems/cheapest-meeting?&utm_source=clipboard&utm_medium=text

import math

INT_MAX = math.inf

n, m = map(int, input().split())
v1, v2, e = map(int, input().split())

dist = [[INT_MAX] * (n + 1) for _ in range(n + 1)]

for i in range(1, n+1):
    dist[i][i] = 0

for _ in range(m):
    x, y, z = tuple(map(int, input().split()))
    dist[x][y] = dist[y][x] = z

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = INT_MAX

for k in range(1, n+1):
    ans = min(ans, dist[v1][k] + dist[v2][k] + dist[k][e])

if ans == INT_MAX:
    ans = -1

print(ans)