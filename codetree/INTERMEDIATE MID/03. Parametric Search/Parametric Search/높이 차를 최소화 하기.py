# problem link : https://www.codetree.ai/missions/8/problems/minimize-the-height-difference?&utm_source=clipboard&utm_medium=text

import sys
sys.setrecursionlimit(10000)

MAX_H = 500

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
visited = [[0] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def dfs(x, y, lo, hi):
    if visited[x][y]:
        return
    
    visited[x][y] = True
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if in_range(nx, ny) and board[nx][ny] >= lo and board[nx][ny] <= hi:
            dfs(nx, ny, lo, hi)

def clear_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False

def reachable(d):
    for lo in range(1, MAX_H + 1):
        clear_visited()

        hi = lo + d
        
        if board[0][0] >= lo and board[0][0] <= hi:
            dfs(0, 0, lo, hi)

        if visited[n-1][m-1]:
            return True
    
    return False

lo = 0
hi = MAX_H
ans = MAX_H

while lo <= hi:
    mid = (lo + hi) // 2
    if reachable(mid):
        hi = mid - 1
        ans = min(ans, mid)
    else:
        lo = mid + 1

print(ans)