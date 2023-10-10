# problem link : https://www.codetree.ai/training-field/frequent-problems/problems/artistry?&utm_source=clipboard&utm_medium=text

# dfs method

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
next_arr = [
    [0] * n
    for _ in range(n)
]

group_n = 0
group = [
    [0] * n
    for _ in range(n)
]

group_cnt = [0] * (n * n + 1)
visited = [
    [False] * n
    for _ in range(n)
]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def dfs(x, y):
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny) and not visited[nx][ny] and arr[nx][ny] == arr[x][y]:
            visited[nx][ny] = True
            group[nx][ny] = group_n
            group_cnt[group_n] += 1
            dfs(nx, ny)

def make_group():
    global group_n

    group_n = 0

    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                group_n += 1
                visited[i][j] = True
                group[i][j] = group_n
                group_cnt[group_n] = 1
                dfs(i, j)

def get_art_score():
    art_score = 0

    for i in range(n):
        for j in range(n):
            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy

                if in_range(nx, ny) and arr[i][j] != arr[nx][ny]:
                    g1, g2 = group[i][j], group[nx][ny]
                    num1, num2 = arr[i][j], arr[nx][ny]
                    cnt1, cnt2 = group_cnt[g1], group_cnt[g2]

                    art_score += (cnt1 + cnt2) * num1 * num2

    return art_score // 2

def get_score():
    make_group()

    return get_art_score()

def rotate_square(sx, sy, square_n):
    for x in range(sx, sx + square_n):
        for y in range(sy, sy + square_n):
            ox, oy = x - sx, y - sy
            rx, ry = oy, square_n - ox - 1
            next_arr[rx + sx][ry + sy] = arr[x][y]

def rotate():
    for i in range(n):
        for j in range(n):
            next_arr[i][j] = 0

    for i in range(n):
        for j in range(n):
            if j == n // 2:
                next_arr[j][i] = arr[i][j]
            elif i == n // 2:
                next_arr[n - j - 1][i] = arr[i][j]

    sqaure_n = n // 2
    rotate_square(0, 0, sqaure_n)
    rotate_square(0, sqaure_n + 1, sqaure_n)
    rotate_square(sqaure_n + 1, 0, sqaure_n)
    rotate_square(sqaure_n + 1, sqaure_n + 1, sqaure_n)

    for i in range(n):
        for j in range(n):
            arr[i][j] = next_arr[i][j]

ans = 0
for _ in range(4):
    ans += get_score()

    rotate()

print(ans)

# bfs method

from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def group_num(x, y, number):
    Q = deque()
    Q.append((x, y))
    visit[x][y] = 1
    group[x][y] = number
    group_cnt[number] += 1
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == graph[x][y] and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                group[nx][ny] = number
                group_cnt[number] += 1
                Q.append((nx, ny))


def score():
    result = 0
    for i in range(n):
        for j in range(n):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] != graph[i][j]:
                        gx, gy = group[i][j], group[nx][ny]
                        gxnum, gynum = graph[i][j], graph[nx][ny]
                        gxcnt, gycnt = group_cnt[gx], group_cnt[gy]
                        result += (gxcnt + gycnt) * gxnum * gynum

    return result // 2

def cross_rotate():
    for i in range(n):
        for j in range(n):
            if i == n//2:
                arr[i][j] = graph[j][i]
            if j == n//2:
                arr[i][j] = graph[n-j-1][n-i-1]

def square_rotate(x, y, l):
    for i in range(x, x+l):
        for j in range(y, y+l):
            ox, oy = i - x, j - y
            rx, ry = oy, l - ox - 1
            arr[rx+x][ry+y] = graph[i][j]

answer = 0
for _ in range(4):
    group = [[0]*n for _ in range(n)]
    group_cnt = [0]*(n*n+1)
    numbers = 0
    visit = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                numbers += 1
                group_num(i, j, numbers)


    answer += score()
    arr = [[0]*n for _ in range(n)]
    half = n//2
    cross_rotate()

    square_rotate(0, 0, half)
    square_rotate(0, half+1, half)
    square_rotate(half+1, 0, half)
    square_rotate(half+1, half+1, half)

    for i in range(n):
        for j in range(n):
            graph[i][j] = arr[i][j]

print(answer)