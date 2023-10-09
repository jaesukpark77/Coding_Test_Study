# problem link : https://www.codetree.ai/missions/2/problems/knight-movements?&utm_source=clipboard&utm_medium=text

import math
from collections import deque

INT_MAX = math.inf

n = int(input())
r1, c1, r2, c2 = tuple(map(int, input().split()))

q = deque()
visited = [[False for _ in range(n)] for _ in range(n)]
step = [[0 for _ in range(n)] for _ in range(n)]

ans = INT_MAX

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    return in_range(x, y) and not visited[x][y]

def push(nx, ny, ns):
    q.append((nx, ny))
    visited[nx][ny] = True
    step[nx][ny] = ns

def find_min():
    global ans

    while q:
        x, y = q.popleft()
        dxs = [-2, -2, -1, -1, 1, 1, 2, 2]
        dys = [-1, 1, -2, 2, -2, 2, -1, 1]

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                push(nx, ny, step[x][y] + 1)

    if visited[r2 - 1][c2 - 1]:
        ans = step[r2 - 1][c2 - 1]

push(r1 - 1, c1 - 1, 0)
find_min()

if ans == INT_MAX:
    ans = -1

print(ans)