# problem link : https://www.codetree.ai/missions/2/problems/escape-with-min-distance?&utm_source=clipboard&utm_medium=text

import math
from collections import deque

INT_MAX = math.inf

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

q = deque()
visited = [[False] * m for _ in range(n)]
step = [[0 for _ in range(m)] for _ in range(n)]

ans = INT_MAX

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    return in_range(x, y) and a[x][y] and not visited[x][y]

def push(new_x, new_y, new_step):
    q.append((new_x, new_y))
    visited[new_x][new_y] = True
    step[new_x][new_y] = new_step

def find_min():
    global ans

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if can_go(new_x, new_y):
                push(new_x, new_y, step[x][y] + 1)

    if visited[n -1][m - 1]:
        ans = step[n - 1][m - 1]

push(0, 0, 0)
find_min()

if ans == INT_MAX:
    ans = -1

print(ans)