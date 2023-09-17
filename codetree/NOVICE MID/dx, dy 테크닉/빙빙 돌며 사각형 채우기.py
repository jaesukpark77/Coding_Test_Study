# problem link : https://www.codetree.ai/missions/5/problems/snail-alphabet-square?&utm_source=clipboard&utm_medium=text

n, m = map(int, input().split())
answer = [[0] * m for _ in range(n)]
visited =[[0] * m for _ in range(n)]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
curr_x, curr_y = 0, 0
direction = 0

answer[curr_x][curr_y] = 'A'
visited[curr_x][curr_y] = True

def can_go(new_x, new_y):
    if 0 <= new_x and new_x < n and 0 <= new_y and new_y < m and visited[new_x][new_y] == 0:
        return True
    else:
        return False

for i in range(1, n * m):
    while True:
        next_x, next_y = curr_x + dxs[direction], curr_y + dys[direction]

        if can_go(next_x, next_y):
            curr_x, curr_y = next_x, next_y
            visited[curr_x][curr_y] = True
            answer[curr_x][curr_y] = chr((i % 26) + ord('A'))
            break
        else:
            direction = (direction + 1) % 4

for i in range(n):
    for j in range(m):
        print(answer[i][j], end=' ')
    print()