# problem link : https://www.codetree.ai/missions/5/problems/snail-start-from-center?&utm_source=clipboard&utm_medium=text

n = int(input())
grid = [[0] * n for _ in range(n)]

curr_x, curr_y = n // 2, n // 2
move_dir, move_num = 0, 1

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def move():
    global curr_x, curr_y

    dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]
    curr_x, curr_y = curr_x + dxs[move_dir], curr_y + dys[move_dir]

def end():
    return not in_range(curr_x, curr_y)

cnt = 1

while not end():
    for _ in range(move_num):
        grid[curr_x][curr_y] = cnt
        cnt += 1

        move()

        if end():
            break

    move_dir = (move_dir + 1) % 4

    if move_dir == 0 or move_dir == 2:
        move_num += 1
    
for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()