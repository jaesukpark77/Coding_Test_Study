# problem link : https://www.codetree.ai/missions/2/problems/move-to-larger-adjacent-cell?&utm_source=clipboard&utm_medium=text

n = int(input())
x, y = 0, 0
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

for _ in range(n):
    c_dir, dist = input().split()
    dist = int(dist)

    if c_dir == 'E':
        move_dir = 0
    elif c_dir == 'W':
        move_dir = 1
    elif c_dir == 'S':
        move_dir = 2
    else:
        move_dir = 3

    x += dx[move_dir] * dist
    y += dy[move_dir] * dist

print(x, y)