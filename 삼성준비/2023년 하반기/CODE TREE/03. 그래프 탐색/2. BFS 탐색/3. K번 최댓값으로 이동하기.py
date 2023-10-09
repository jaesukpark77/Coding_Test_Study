# problem link : https://www.codetree.ai/missions/2/problems/move-to-max-k-times?&utm_source=clipboard&utm_medium=text

from collections import deque

NOT_EXIST = (-1, -1)

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

r, c = tuple(map(int, input().split()))
curr_cell = (r-1, c-1)

q = deque()
visited = [[False] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y, target_num):
    return in_range(x, y) and not visited[x][y] and grid[x][y] < target_num

def initialize_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    curr_x, curr_y = curr_cell
    visited[curr_x][curr_y] = True
    q.append(curr_cell)

    target_num = grid[curr_x][curr_y]

    while q:
        curr_x, curr_y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = curr_x + dx, curr_y + dy

            if can_go(nx, ny, target_num):
                q.append((nx, ny))
                visited[nx][ny] = True

# best 위치를 새로운 위치로 바꿔줘야 하는지를 판단
def need_update(best_pos, new_pos):
    # 첫 도달 가능한 위치라면 update가 필요
    if best_pos == NOT_EXIST:
        return True
    
    best_x, best_y = best_pos
    new_x, new_y = new_pos

    # 숫자, -행, -열 순으로 더 큰 곳이 골라져야 합니다.
    return (grid[new_x][new_y], -new_x, -new_y) > (grid[best_x][best_y], -best_x, -best_y)

# 가장 우선순위가 높은 위치를 찾아 위치를 이동
def move():
    global curr_cell

    initialize_visited()
    bfs()

    best_pos = NOT_EXIST
    for i in range(n):
        for j in range(n):
            if not visited[i][j] or (i, j) == curr_cell:
                continue
            
            new_pos = (i, j)

            if need_update(best_pos, new_pos):
                best_pos = new_pos

    if best_pos == NOT_EXIST:
        return False
    else:
        curr_cell = best_pos
        return True

for _ in range(k):
    is_moved = move()

    if not is_moved:
        break

final_x, final_y = curr_cell
print(final_x + 1, final_y + 1)