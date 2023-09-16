# problem link : https://www.codetree.ai/missions/5/problems/text-based-commands2?&utm_source=clipboard&utm_medium=text

dirs = input()
x, y = 0, 0
curr_dir = 3

dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

for c_dir in dirs:
    if c_dir == 'L':
        curr_dir = (curr_dir - 1 + 4) % 4
    elif c_dir == 'R':
        curr_dir = (curr_dir + 1) % 4
    else:
        x, y = x + dxs[curr_dir], y + dys[curr_dir]

print(x, y)