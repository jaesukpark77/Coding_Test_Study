# problem link : https://www.codetree.ai/missions/8/problems/pair-of-points-that-can-be-moved?&utm_source=clipboard&utm_medium=text

import math

INT_MAX = math.inf

n, m, p, q = map(int, input().split())

dist = [[INT_MAX] * (n + 1) for _ in range(n+1)]

for i in range(1, n+1):
    dist[i][i] = 0

for _ in range(m):
    x, y, z = tuple(map(int, input().split()))
    dist[x][y] = z

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = 0
cnt = 0

for _ in range(q):
    x, y = tuple(map(int, input().split()))

    distance = INT_MAX

    for i in range(1, p+1):
        distance = min(distance, dist[x][i] + dist[i][y])

    if distance >= INT_MAX:
        continue

    ans += distance
    cnt += 1

print(cnt)
print(ans)