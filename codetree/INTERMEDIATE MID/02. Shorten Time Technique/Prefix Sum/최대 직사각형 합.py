# problem link : https://www.codetree.ai/missions/8/problems/max-rect-sum-in-grid?&utm_source=clipboard&utm_medium=text

import math

INT_MIN = -math.inf

n = int(input())

arr = [[0] * (n + 1)]
for _ in range(n):
    arr.append([0] + list(map(int, input().split())))

prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]

def get_sum(x1, y1, x2, y2):
    return prefix_sum[x2][y2] - prefix_sum[x1 -1][y2] - prefix_sum[x2][y1 -1] + prefix_sum[x1 - 1][y1 - 1]

def get_max_area(x1, x2):
    dp = [0] * (n + 1)

    for y in range(1, n + 1):
        value = get_sum(x1, y, x2, y)
        dp[y] = max(value, dp[y - 1] + value)
    
    max_area = INT_MIN
    for y in range(1, n + 1):
        max_area = max(max_area, dp[y])

    return max_area

prefix_sum[0][0] = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + arr[i][j]

ans = INT_MIN
for i in range(1, n + 1):
    for j in range(i, n + 1):
        ans = max(ans, get_max_area(i, j))

print(ans)