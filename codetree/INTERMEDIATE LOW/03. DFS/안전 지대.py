# problem link : https://www.codetree.ai/missions/2/problems/comfort-zone?&utm_source=clipboard&utm_medium=text

import sys
sys.setrecursionlimit(2500)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

zone_num = 0

def initialize_vistied():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y, k):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] <= k:
        return False
    
    return True

def dfs(x, y, k):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y, k):
            visited[new_x][new_y] = True
            dfs(new_x, new_y, k)

def get_zone_num(k):
    global zone_num

    zone_num = 0
    initialize_vistied()

    for i in range(n):
        for j in range(m):
            if can_go(i, j, k):
                visited[i][j] = True
                zone_num += 1

                dfs(i, j, k)

max_zone_num = -1
answer_k = 0
max_height = 100

for k in range(1, max_height + 1):
    get_zone_num(k)

    if zone_num > max_zone_num:
        max_zone_num, answer_k = zone_num, k

print(answer_k, max_zone_num)