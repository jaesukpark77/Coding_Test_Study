# problem link : https://www.codetree.ai/missions/9/problems/tree-identification?&utm_source=clipboard&utm_medium=text

MAX_N = 10000

m = int(input())
root = 0
deg = [0] * (MAX_N + 1)
edges = [[] for _ in range(MAX_N + 1)]
used = [False] * (MAX_N + 1)
visited = [False] * (MAX_N + 1)
is_tree = True

for _ in range(m):
    x, y = tuple(map(int, input().split()))
    edges[x].append(y)

    used[x] = True
    used[y] = True

    deg[y] += 1

def dfs(x):
    for y in edges[x]:
        if visited[y]:
            continue

        visited[y] = True
        dfs(y)

    return

for i in range(1, MAX_N + 1):
    if used[i] and deg[i] == 0:
        if root != 0:
            is_tree = False
        root = i

if root == 0:
    is_tree = False

for i in range(1, MAX_N + 1):
    if used[i] and i != root and deg[i] != 1:
        is_tree = False

if is_tree and root != 0:
    visited[root] = True
    dfs(root)

for i in range(1, MAX_N + 1):
    if used[i] and not visited[i]:
        is_tree = False

if is_tree: 
    print(1)
else:
    print(0)