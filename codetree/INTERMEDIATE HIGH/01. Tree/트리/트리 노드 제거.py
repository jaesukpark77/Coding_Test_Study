# problem link : https://www.codetree.ai/missions/9/problems/remove-tree-node?&utm_source=clipboard&utm_medium=text

n = int(input())
ans = 0
root = -1
edges = [[] for _ in range(n)]
is_deleted = [False] * (n)

par = list(map(int, input().split()))

for i in range(n):
    x, y = i, par[i]

    if y == -1:
        root = x
        continue

    edges[y].append(x)

del_node = int(input())

def dfs(x):
    global ans

    if is_deleted[x]:
        return
    
    is_leaf = True

    for y in edges[x]:
        if is_deleted[y]:
            continue
        
        dfs(y)

        is_leaf = False
    
    if is_leaf:
        ans += 1

is_deleted[del_node] = True
dfs(root)

print(ans)