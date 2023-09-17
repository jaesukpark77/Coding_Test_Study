# problem link : https://www.codetree.ai/missions/5/problems/small-marble-movement?&utm_source=clipboard&utm_medium=text

n, t = map(int, input().split())
x, y, curr_dir = input().split()
x, y = int(x), int(y)

direction = {
    'R' : 0,
    'D' : 1,
    'U' : 2,
    'L' : 3
}

x, y, move_dir = x - 1, y - 1, direction[curr_dir]

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for _ in range(t):
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    if in_range(nx, ny):
        x, y = nx, ny
    else:
        move_dir = 3 - move_dir

print(x + 1, y + 1)