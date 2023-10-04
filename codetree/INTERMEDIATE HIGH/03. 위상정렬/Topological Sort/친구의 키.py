# problem link : https://www.codetree.ai/missions/9/problems/height-of-friends?&utm_source=clipboard&utm_medium=text

# DFS 활용

import sys

sys.setrecursionlimit(100000)

n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
reversed_order = []

for _ in range(m):
    x, y = tuple(map(int, input().split()))
    edges[x].append(y)

def dfs(x):
    for y in edges[x]:
        if not visited[y]:
            visited[y] = True
            dfs(y)

    reversed_order.append(x)

for i in range(1, n+1):
    if not visited[i]:
        visited[i] = True
        dfs(i)

for num in reversed_order[::-1]:
    print(num, end=' ')

# Indegree 활용

from collections import deque

n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]

indegree = [0] * (n+1)

q = deque()

for _ in range(m):
    x, y = tuple(map(int, input().split()))

    edges[x].append(y)
    indegree[y] += 1

for i in range(1, n+1):
    if not indegree[i]:
        q.append(i)

while q:
    x = q.popleft()
    print(x, end=' ')

    for y in edges[x]:
        indegree[y] -= 1

        if not indegree[y]:
            q.append(y)