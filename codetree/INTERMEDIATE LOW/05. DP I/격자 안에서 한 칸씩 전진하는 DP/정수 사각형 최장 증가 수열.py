# problem link : https://www.codetree.ai/missions/2/problems/lis-on-the-integer-grid?&utm_source=clipboard&utm_medium=text

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp =[[0] * n for _ in range(n)]

cells = []
ans = 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for i in range(n):
    for j in range(n):
        cells.append((grid[i][j], i, j))

cells.sort()

for i in range(n):
    for j in range(n):
        dp[i][j] = 1

for _, x, y in cells:
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny) and grid[nx][ny] > grid[x][y]:
            dp[nx][ny] = max(dp[nx][ny], dp[x][y] + 1)

for i in range(n):
    for j in range(n):
        ans = max(ans, dp[i][j])

print(ans)