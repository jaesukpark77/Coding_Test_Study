# problem link : https://www.codetree.ai/missions/2/problems/places-can-go?&utm_source=clipboard&utm_medium=text

from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
bfs_q = deque()

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    return in_range(x, y) and not grid[x][y] and not visited[x][y]

def bfs():
    while bfs_q:
        x, y = bfs_q.popleft()

        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                bfs_q.append((nx, ny))
                visited[nx][ny] = True

for _ in range(k):
    x, y = tuple(map(int, input().split()))
    bfs_q.append((x -1, y - 1))
    visited[x - 1][y - 1] = True

bfs()

ans = sum([
    1
    for i in range(n)
    for j in range(n)
    if visited[i][j]
])

print(ans)