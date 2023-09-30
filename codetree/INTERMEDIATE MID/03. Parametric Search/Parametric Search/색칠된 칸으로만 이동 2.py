# problem link : https://www.codetree.ai/missions/8/problems/move-to-the-colored-space-only-2?&utm_source=clipboard&utm_medium=text

from collections import deque

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
colored = [list(map(int, input().split())) for _ in range(m)]

dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]

start_x, start_y = 0, 0
visited = [[False] * n for _ in range(m)]

def in_range(x, y):
    return 0 <= x and x < m and 0 <= y and y < n

def bfs(d):
    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = True

    while q:
        p = q.popleft()

        for (dx, dy) in zip(dxs, dys):
            next_x = p[0] + dx
            next_y = p[1] + dy
            if in_range(next_x, next_y):
                if not visited[next_x][next_y] and abs(board[p[0]][p[1]] - board[next_x][next_y]) <= d:
                    q.append((next_x, next_y))
                    visited[next_x][next_y] = True

def reachable(d):
    for i in range(m):
        for j in range(n):
            visited[i][j] = False

    bfs(d)

    for i in range(m):
        for j in range(n):
            if colored[i][j] and not visited[i][j]:
                return False

    return True

    if colored[i][j]:
        start_x = i
        start_y = j

lo = 0
hi = 1000000000
ans = 0

while lo <= hi:
    mid = (lo + hi) // 2
    if reachable(mid):
        hi = mid - 1
        ans = mid
    else:
        lo = mid + 1

print(ans)