# problem link : https://www.codetree.ai/missions/2/problems/select-proper-clothes?&utm_source=clipboard&utm_medium=text

import math

INT_MIN = -math.inf

n, m = map(int, input().split())

s = [0] * (n + 1)
e = [0] * (n + 1)
v = [0] * (n + 1)

dp = [[0] * (n + 1) for _ in range(m + 1)]

def initialize():
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = INT_MIN
        
    for j in range(1, n + 1):
        if s[j] == 1:
            dp[1][j] = 0

for i in range(1, n+1):
    s[i], e[i], v[i] = tuple(map(int, input().split()))

initialize()

for i in range(2, m + 1):

    for j in range(1, n + 1):
        for k in range(1, n + 1):            
            if s[k] <= i - 1 and i - 1 <= e[k] and s[j] <= i and i <= e[j]:
                dp[i][j] = max(dp[i][j], dp[i - 1][k] + abs(v[j] - v[k]))

ans = max(dp[m][1:n+1])

print(ans)