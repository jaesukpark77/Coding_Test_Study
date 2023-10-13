# problem link : https://www.codetree.ai/training-field/frequent-problems/problems/colored-bomb?&utm_source=clipboard&utm_medium=text

from collections import deque

RED = 0
ROCK = -1
EMPTY = -2
EMPTY_BUNDLE = (-1, -1, -1, -1)

n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

temp = [
    [EMPTY] * n
    for _ in range(n)
]

bfs_q = deque()
visited = [
    [False] * n
    for _ in range(n)
]

ans = 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y, color):
    return in_range(x, y) and not visited[x][y] and (grid[x][y] == color or grid[x][y] == RED)

def bfs(x, y, color):
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    visited[x][y] = True
    bfs_q.append((x, y))

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    while bfs_q:
        curr_x, curr_y = bfs_q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = curr_x + dx, curr_y + dy

            if can_go(nx, ny, color):
                bfs_q.append((nx, ny))
                visited[nx][ny] = True

def get_bundle(x, y):
    bfs(x, y, grid[x][y])

    bomb_cnt, red_cnt = 0, 0
    standard = (-1, -1)

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                continue

            bomb_cnt += 1

            if grid[i][j] == RED:
                red_cnt += 1        
            elif (i, -j) > standard:
                standard = (i, -j)

    std_x, std_y = standard

    return (bomb_cnt, -red_cnt, std_x, -std_y)

def find_best_bundle():
    best_bundle = EMPTY_BUNDLE

    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 1:
                bundle = get_bundle(i, j)
                if bundle > best_bundle:
                    best_bundle = bundle

    return best_bundle

def remove():
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                grid[i][j] = EMPTY

def gravity():
    for i in range(n):
        for j in range(n):
            temp[i][j] = EMPTY

    for j in range(n):
        last_idx = n - 1
        for i in range(n - 1, -1, -1):
            if grid[i][j] == EMPTY:
                continue
            if grid[i][j] == ROCK:
                last_idx = i
            temp[last_idx][j] = grid[i][j]
            last_idx -= 1

    for i in range(n):
        for j in range(n):
            grid[i][j] = temp[i][j]

def rotate():
    for i in range(n):
        for j in range(n):
            temp[i][j] = EMPTY

    for j in range(n - 1, -1, -1):
        for i in range(n):
            temp[n - 1 - j][i] = grid[i][j]

    for i in range(n):
        for j in range(n):
            grid[i][j] = temp[i][j]

def clean(x, y):
    bfs(x, y, grid[x][y])

    remove()

    gravity()

def simulate():
    global ans
    best_bundle = find_best_bundle()
    bomb_cnt, _, x, y = best_bundle

    if best_bundle == EMPTY or bomb_cnt <= 1:
        return False

    ans +=  bomb_cnt * bomb_cnt
    clean(x, -y)

    rotate()

    gravity()

    return True

while True:
    keep_going = simulate()

    if not keep_going:
        break

print(ans)