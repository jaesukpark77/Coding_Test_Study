# problem link : https://www.codetree.ai/missions/8/problems/shortest-distance?&utm_source=clipboard&utm_medium=text

n, m = map(int, input().split())

dist = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for _ in range(m):
    x, y = tuple(map(int, input().split()))

    print(dist[x-1][y-1])