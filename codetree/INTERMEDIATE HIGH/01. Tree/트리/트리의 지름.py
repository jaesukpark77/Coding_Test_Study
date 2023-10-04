# problem link : https://www.codetree.ai/missions/9/problems/diameter-of-tree?&utm_source=clipboard&utm_medium=text

import sys
sys.setrecursionlimit(100000)

n = int(input())
edges = [[] for _ in range(n+1)]
visited = [False] * (n+1)
dist = [0] * (n + 1)

for _ in range(n-1):
    x, y, d = tuple(map(int, input().split()))
    edges[x].append((y, d))
    edges[y].append((x, d))

def dfs(x, total_dist):
    for y, d in edges[x]:
        if not visited[y]:
            visited[y] = True
            dist[y] = total_dist + d
            dfs(y, total_dist + d)

def find_largest_vertex(x):
    for i in range(1, n+1):
        visited[i] = False
        dist[i] = 0

    visited[x] = True
    dist[x] = 0
    dfs(x, 0)

    farthest_dist = -1
    farthest_vertex = -1

    for i in range(1, n+1):
        if dist[i] > farthest_dist:
            farthest_dist = dist[i]
            farthest_vertex = i

    return farthest_vertex, farthest_dist

f_vertex, _ = find_largest_vertex(1)

_, diameter = find_largest_vertex(f_vertex)

print(diameter)