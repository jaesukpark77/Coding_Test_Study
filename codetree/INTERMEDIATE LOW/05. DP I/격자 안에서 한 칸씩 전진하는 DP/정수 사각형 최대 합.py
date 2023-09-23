# problem link : https://www.codetree.ai/missions/2/problems/maximum-sum-path-in-square?&utm_source=clipboard&utm_medium=text

# DP - Memoization Method

UNUSED = -1

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

memo = [[UNUSED for _ in range(n)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def find_max_sum(x, y):
    if memo[x][y] != UNUSED:
        return memo[x][y]

    if x == n - 1 and y == n - 1:
        return grid[n - 1][n - 1]

    dxs, dys = [1, 0], [0, 1]

    max_sum = 0
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if in_range(new_x, new_y):
            max_sum = max(max_sum, find_max_sum(new_x, new_y) + grid[x][y])

    memo[x][y] = max_sum
    return max_sum

print(find_max_sum(0, 0))

# DP - Tabulation Method

n = int(input())

num = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]

def initialize():
    dp[0][0] = num[0][0]

    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + num[i][0]
    
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + num[0][j]

initialize()

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + num[i][j]

print(dp[n-1][n-1])