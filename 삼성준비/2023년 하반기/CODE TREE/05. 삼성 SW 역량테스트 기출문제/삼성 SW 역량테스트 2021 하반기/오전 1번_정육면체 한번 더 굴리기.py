# problem link : https://www.codetree.ai/training-field/frequent-problems/problems/cube-rounding-again?&utm_source=clipboard&utm_medium=text

from collections import deque

FACE_NUM = 6
OUT_OF_GRID = (-1, -1)

n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

x, y = 0, 0
move_dir = 0

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

up, front, right = 1, 2, 3

bfs_q = deque()
visited = [
    [False] * n
    for _ in range(n)
]

ans = 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y, target_num):
    return in_range(x, y) and not visited[x][y] and grid[x][y] == target_num

def bfs(x, y, target_num):
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    visited[x][y] = True
    bfs_q.append((x, y))

    score = 0

    while bfs_q:
        curr_x, curr_y = bfs_q.popleft()
        score += target_num

        for dx, dy in zip(dxs, dys):
            nx, ny = curr_x + dx, curr_y + dy

            if can_go(nx, ny, target_num):
                bfs_q.append((nx, ny))
                visited[nx][ny] = True

    return score

def get_score():
    return bfs(x, y, grid[x][y])

def next_pos():
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    return (nx, ny) if in_range(nx, ny) else OUT_OF_GRID

def simulate():
    global ans
    global x, y, move_dir
    global up, front, right

    nx, ny = next_pos()

    if (nx, ny) == OUT_OF_GRID:
        move_dir = (move_dir + 2) if move_dir < 2 else (move_dir - 2)
        nx, ny = next_pos()

    x, y = nx, ny

    ans += get_score()

    if move_dir == 0:
        up, front, right = 7 - right, front, up
    elif move_dir == 1:
        up, front, right = 7 - front, up, right
    elif move_dir == 2:
        up, front, right = right, front, 7 - up
    else:
        up, front, right = front, 7 - up, right

    bottom = 7 - up

    if bottom > grid[x][y]:
        move_dir = (move_dir + 1) % 4
    elif bottom < grid[x][y]:
        move_dir = (move_dir -1 + 4) % 4

for _ in range(m):
    simulate()

print(ans)