# problem link : https://www.codetree.ai/missions/5/problems/comfortable-state-on-the-grid?&utm_source=clipboard&utm_medium=text

n, m = map(int, input().split())
arr = [[0] * n for _ in range(n)]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def adjacent_cnt(x,y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny] == 1:
            cnt += 1
    
    return cnt

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    arr[x][y] = 1

    if adjacent_cnt(x, y) == 3:
        print(1)
    else:
        print(0)