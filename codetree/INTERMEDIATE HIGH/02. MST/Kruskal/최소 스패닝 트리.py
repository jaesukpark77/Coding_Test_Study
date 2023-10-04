# problem link : https://www.codetree.ai/missions/9/problems/minimum-spanning-tree?&utm_source=clipboard&utm_medium=text

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

uf = [0] * (n+1)

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])

    return uf[x]

def union(x, y):
    x, y = find(x), find(y)
    uf[x] = y

edges.sort(key = lambda x:x[2])

for i in range(1, n+1):
    uf[i] = i

ans = 0

for x, y, cost in edges:
    if find(x) != find(y):
        ans += cost
        union(x, y)

print(ans)