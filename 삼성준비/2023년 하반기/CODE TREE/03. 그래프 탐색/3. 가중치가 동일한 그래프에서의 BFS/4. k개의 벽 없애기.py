# problem link : https://www.codetree.ai/missions/2/problems/remove-k-walls?&utm_source=clipboard&utm_medium=text

import math
from collections import deque

INT_MAX = math.inf

n, k = tuple(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = tuple(map(int, input().split()))
r2, c2 = tuple(map(int, input().split()))
r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

stone_pos = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if a[i][j]
]

q = deque()
visited = [[False] * n for _ in range(n)]
step = [[0] * n for _ in range(n)]
ans = INT_MAX

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    return in_range(x, y) and not a[x][y] and not visited[x][y]

def push(nx, ny, ns):
    q.append((nx, ny))
    visited[nx][ny] = True
    step[nx][ny] = ns

def bfs():
    while q:
        x, y = q.popleft()

        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                push(nx, ny, step[x][y] + 1)

    if visited[r2][c2]:
        return step[r2][c2]
    else:
        return INT_MAX

def find_min(idx, cnt):
    global ans

    if idx == len(stone_pos):
        if cnt == k:
            for i in range(n):
                for j in range(n):
                    visited[i][j] = False
                    step[i][j] = 0

            push(r1, c1, 0)
            min_dist = bfs()
            ans = min(ans, min_dist)

        return
    
    x, y = stone_pos[idx]
    a[x][y] = 0
    find_min(idx + 1, cnt + 1)
    a[x][y] = 1

    find_min(idx + 1, cnt)

find_min(0, 0)

if ans == INT_MAX:
    ans = -1

print(ans)