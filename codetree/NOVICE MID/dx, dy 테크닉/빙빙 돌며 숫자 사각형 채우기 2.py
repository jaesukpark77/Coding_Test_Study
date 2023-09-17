# problem link : https://www.codetree.ai/missions/5/problems/snail-number-square-2?&utm_source=clipboard&utm_medium=text

n, m = map(int, input().split())
answer = [[0] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
dir_num = 1

answer[x][y] = 1

for i in range(2, n * m + 1):
    while True:
        nx, ny = x + dxs[dir_num], y + dys[dir_num]

        if in_range(nx, ny) and answer[nx][ny] == 0:
            x, y = nx, ny
            answer[x][y] = i
            break
        else:
            dir_num = (dir_num + 3) % 4

for i in range(n):
    for j in range(m):
        print(answer[i][j], end=' ')
    print()