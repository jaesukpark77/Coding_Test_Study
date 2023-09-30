# problem link : https://www.codetree.ai/missions/8/problems/painting-the-grid-2?&utm_source=clipboard&utm_medium=text

import sys

sys.setrecursionlimit(10000)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [1, -1, 0, 0], [0, 0, -1, 1]
visited = [[False] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def dfs(x, y, d):
    if visited[x][y]:
        return 0

    visited[x][y] = True
    count = 1
    for dx, dy in zip(dxs, dys):
        next_x = x + dx
        next_y = y + dy

        if in_range(next_x, next_y) and (abs(board[next_x][next_y] - board[x][y]) <= d):
            count += dfs(next_x, next_y, d)

    return count

def is_possible(d):
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if dfs(i, j, d) * 2 >= n * n:
                    return True

    return False

lo = 0
hi = 1000000
ans = 0

while lo <= hi:
    mid = (lo + hi) // 2
    if is_possible(mid):
        hi = mid - 1
        ans = mid
    else:
        lo = mid + 1

print(ans)