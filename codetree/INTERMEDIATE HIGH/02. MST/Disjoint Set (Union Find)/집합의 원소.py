# problem link : https://www.codetree.ai/missions/9/problems/elements-of-a-set?&utm_source=clipboard&utm_medium=text

n, m = map(int, input().split())
uf = [0] * (n + 1)

for i in range(1, n+1):
    uf[i] = i

def find(x):
    if uf[x] == x:
        return x

    uf[x] = find(uf[x])
    return uf[x]

def union(x, y):
    x, y = find(x), find(y)
    uf[x] = y

for _ in range(m):
    q_type, a, b = tuple(map(int, input().split()))

    if q_type == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print(1)
        else:
            print(0)