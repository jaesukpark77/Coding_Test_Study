# problem link : https://www.codetree.ai/training-field/frequent-problems/problems/artistry?&utm_source=clipboard&utm_medium=text

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