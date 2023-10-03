# problem link : https://www.codetree.ai/missions/8/problems/size-comparison?&utm_source=clipboard&utm_medium=text

n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n+1)]

for _ in range(m):
    x, y = tuple(map(int, input().split()))
    graph[x][y] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if i == j:
            continue
        if graph[i][j] or graph[j][i]:
            continue
        cnt += 1
    print(cnt)