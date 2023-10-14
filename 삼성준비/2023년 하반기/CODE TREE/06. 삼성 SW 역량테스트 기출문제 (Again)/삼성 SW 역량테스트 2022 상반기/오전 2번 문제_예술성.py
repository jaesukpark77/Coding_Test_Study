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