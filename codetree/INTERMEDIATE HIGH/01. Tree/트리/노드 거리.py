# problem link : https://www.codetree.ai/missions/9/problems/node-distance?&utm_source=clipboard&utm_medium=text

n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
dist = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(n - 1):
    x, y, d = tuple(map(int, input().split()))

    edges[x].append((y, d))
    edges[y].append((x, d))

def dfs(st, x):
    for y, d in edges[x]:
        if visited[y]:
            continue
        
        visited[y] = True

        dist[st][y] = dist[st][x] + d
        dfs(st, y)

for i in range(1, n+1):
    for j in range(1, n+1):
        visited[j] = False

    visited[i] = True
    dfs(i, i)

for _ in range(m):
    x, y = tuple(map(int, input().split()))
    print(dist[x][y])