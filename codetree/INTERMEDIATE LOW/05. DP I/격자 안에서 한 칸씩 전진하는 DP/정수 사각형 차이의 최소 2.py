# problem link : https://www.codetree.ai/missions/2/problems/minimum-difference-on-the-integer-grid-2?&utm_source=clipboard&utm_medium=text

import math

INT_MAX = math.inf
MAX_R = 100

n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

ans = INT_MAX

def initialize():
    for i in range(n):
        for j in range(n):
            dp[i][j] = INT_MAX

    dp[0][0] = num[0][0]

    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], num[i][0])

    for j in range(1, n):
        dp[0][j] = max(dp[0][j-1], num[0][j])

def solve(lower_bound):
    for i in range(n):
        for j in range(n):
            if num[i][j] < lower_bound:
                num[i][j] = INT_MAX

    initialize()

    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max((min(dp[i-1][j], dp[i][j-1]), num[i][j]))

    return dp[n-1][n-1]

for lower_bound in range(1, MAX_R + 1):
    upper_bound = solve(lower_bound)

    if upper_bound == INT_MAX:
        continue

    ans = min(ans, upper_bound - lower_bound)

print(ans)