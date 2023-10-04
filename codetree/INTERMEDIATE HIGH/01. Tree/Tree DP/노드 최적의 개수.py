# problem link : https://www.codetree.ai/missions/9/problems/node-best-count?&utm_source=clipboard&utm_medium=text

import sys
sys.setrecursionlimit(100000)

n = int(input())
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
parent = [0] * (n + 1)

dp = [[0, 0] for _ in range(n + 1)]

for _ in range(n - 1):
    x, y = tuple(map(int, input().split()))
    edges[x].append(y)
    edges[y].append(x)

def dfs(x):
    for y in edges[x]:
        if not visited[y]:
            visited[y] = True
            parent[y] = x
            dfs(y)

    dp[x][0] = 0
    dp[x][1] = 1

    for y in edges[x]:
        if parent[y] != x:
            continue
        
        dp[x][0] += dp[y][1]

        dp[x][1] += min(dp[y][0], dp[y][1])

visited[1] = True
dfs(1)

print(min(dp[1][0], dp[1][1]))