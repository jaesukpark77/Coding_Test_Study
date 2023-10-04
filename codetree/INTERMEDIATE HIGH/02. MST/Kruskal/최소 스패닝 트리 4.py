# problem link : https://www.codetree.ai/missions/9/problems/minimum-spanning-tree-4?&utm_source=clipboard&utm_medium=text

n, m = tuple(map(int, input().split()))

uf = [0] * (n + 1)
ab_type = [' '] + list(input().split())

edges = [tuple(map(int, input().split())) for _ in range(m)]

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


def union(x, y):
    X, Y = find(x), find(y)
    uf[X] = Y

edges.sort(key=lambda x: x[2])

for i in range(1, n + 1):
    uf[i] = i

ans = 0
for x, y, cost in edges:
    if ab_type[x] == ab_type[y]:
        continue

    if find(x) != find(y):
        ans += cost
        union(x, y)

is_all_connected = True
for i in range(2, n + 1):
    x = find(1)
    y = find(i)
    if x != y: 
        is_all_connected = False

if is_all_connected:
    print(ans)
else:
    print(-1)