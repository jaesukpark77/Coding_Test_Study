# problem link : https://www.codetree.ai/missions/9/problems/graph-and-string?&utm_source=clipboard&utm_medium=text

n, pattern = tuple(input().split())
n = int(n)
l = len(pattern)

edges = [[] for _ in range(n + 1)]
path = [0] * (n + 1)

for _ in range(n - 1):
    x, y, c = tuple(input().split())
    x, y = int(x), int(y)
    edges[x].append((y, c))

p = [31, 37]
m = [int(1e9) + 7, int(1e9) + 9]

p_pow = [[0] * (n + 1) for _ in range(2)]

p_h = [0, 0]

ans = 0

def to_int(c):
    return ord(c) - ord('a') + 1

def dfs(x, cnt, t_h1, t_h2):
    global ans

    t_h = [t_h1, t_h2]

    if cnt == l:
        for k in range(2):
            for i in range(l):
                t_h[k] = (t_h[k] + to_int(path[i]) * p_pow[k][l - 1 - i]) % m[k]
    elif cnt > l:
        for k in range(2):
            t_h[k] = (t_h[k] * p[k] - to_int(path[cnt - l - 1]) * p_pow[k][l] + to_int(path[cnt - 1])) % m[k]
            if t_h[k] < 0:
                t_h[k] += m[k]

    if t_h[0] == p_h[0] and t_h[1] == p_h[1]:
        ans += 1

    for y, c in edges[x]:
        path[cnt] = c
        dfs(y, cnt + 1, t_h[0], t_h[1])

for k in range(2):
    p_pow[k][0] = 1
    for i in range(1, n + 1):
        p_pow[k][i] = (p_pow[k][i - 1] * p[k]) % m[k]

for k in range(2):
    for i in range(l):
        p_h[k] = (p_h[k] + to_int(pattern[i]) * p_pow[k][l - 1 - i]) % m[k]

dfs(1, 0, 0, 0)

print(ans)