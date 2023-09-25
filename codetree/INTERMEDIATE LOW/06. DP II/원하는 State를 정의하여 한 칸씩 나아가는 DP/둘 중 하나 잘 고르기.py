# problem link : https://www.codetree.ai/missions/2/problems/choose-one-of-two-points?&utm_source=clipboard&utm_medium=text

import sys

INT_MIN = -sys.maxsize


n = int(input())
red = [
    0
    for _ in range(2 * n + 1)
]
blue = [
    0
    for _ in range(2 * n + 1)
]

dp = [
    [0 for _ in range(2 * n + 1)]
    for _ in range(2 * n + 1)
]


def initialize():
    for i in range(2 * n + 1):
        for j in range(2 * n + 1):
            dp[i][j] = INT_MIN
    
    dp[0][0] = 0


for i in range(1, 2 * n + 1):
    red[i], blue[i] = tuple(map(int, input().split()))
    
initialize()

for i in range(1, 2 * n + 1):
    for j in range(i + 1):
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + red[i])

        if i - j > 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + blue[i])

print(dp[2 * n][n])