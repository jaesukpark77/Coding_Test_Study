# problem link : https://www.codetree.ai/missions/5/problems/l-r-and-b?&utm_source=clipboard&utm_medium=text

n = 10
board = [input() for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 'L':
            l_x = i
            l_y = j
        if board[i][j] == 'R':
            r_x = i
            r_y = j
        if board[i][j] == 'B':
            b_x = i
            b_y = j

if l_x != b_x and l_y != b_y:
    print(abs(l_x - b_x) + abs(l_y - b_y) - 1)
elif l_y == b_y:
    if l_y == r_y and r_x >= min(b_x, l_x) and r_x <= max(b_x, l_x):
        print(abs(l_x - b_x) + abs(l_y - b_y) + 1)
    else:
        print(abs(l_x - b_x) + abs(l_y - b_y) - 1)
elif l_x == b_x:
    if l_x == r_x and r_y >= min(b_y, l_y) and r_y <= max(b_y, l_y):
        print(abs(l_x - b_x) + abs(l_y - b_y) + 1)
    else:
        print(abs(l_x - b_x) + abs(l_y - b_y) - 1)