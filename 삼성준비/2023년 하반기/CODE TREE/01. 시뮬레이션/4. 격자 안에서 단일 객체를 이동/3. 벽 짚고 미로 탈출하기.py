# problem link : https://www.codetree.ai/missions/2/problems/escape-maze-with-wall-following?&utm_source=clipboard&utm_medium=text

import sys

DIR_NUM = 4

n = int(input())
curr_x, curr_y = map(int, input().split())
a = [[0 for _ in range(n+1)] for _ in range(n+1)]

# 미로 탈출이 불가능한지 여부를 판단하기 위해 동일한 위치에 동일한 방향으로 진행했던 적이 있는지를 표시해주는 배열입니다.
visited = [[[False for _ in range(DIR_NUM)] for _ in range(n + 1)] for _ in range(n+1)]

elasped_time = 0

# 처음에는 우측 방향을 바라보고 시작합니다.
curr_dir = 0

# 범위가 격자 안에 들어가는지 확인합니다.
def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

# 해당 위치에 벽이 있으면 이동이 불가합니다.
def wall_exist(x,y):
    return in_range(x, y) and a[x][y] == '#'

def simualte():
    global curr_x, curr_y, curr_dir, elasped_time

    if visited[curr_x][curr_y][curr_dir]:
        print(-1)
        sys.exit(0)

    visited[curr_x][curr_y][curr_dir] = True

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    next_x, next_y = curr_x + dxs[curr_dir], curr_y + dys[curr_dir]

    if wall_exist(next_x, next_y):
        curr_dir = (curr_dir + 3) % 4
    elif not in_range(next_x, next_y):
        curr_x, curr_y = next_x, next_y
        elasped_time += 1
    else:
        rx = next_x + dxs[(curr_dir + 1) % 4]
        ry = next_y + dys[(curr_dir + 1) % 4]

        if wall_exist(rx, ry):
            curr_x, curr_y = next_x, next_y
            elasped_time += 1
        else:
            curr_x, curr_y = rx, ry
            curr_dir = (curr_dir + 1) % 4
            elasped_time += 2

for i in range(1, n + 1):
    given_row = input()
    for j, elem in enumerate(given_row, start = 1):
        a[i][j] = elem

while in_range(curr_x, curr_y):
    simualte()

print(elasped_time)