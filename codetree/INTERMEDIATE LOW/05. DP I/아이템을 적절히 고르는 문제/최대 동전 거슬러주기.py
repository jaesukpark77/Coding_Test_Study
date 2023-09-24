# problem link : https://www.codetree.ai/missions/2/problems/max-coin-change?&utm_source=clipboard&utm_medium=text

import math

INT_MAX = -math.inf

n, m = map(int, input().split())
coin = [0] + list(map(int, input().split()))

dp = [0] * (m+1)

def initialize():
    for i in range(m+1):
        dp[i] = INT_MAX

    dp[0] = 0

initialize()

for i in range(1, m+1):
    for j in range(1, n+1):
        if i >= coin[j]:
            if dp[i - coin[j]] == INT_MAX:
                continue
            dp[i] = max(dp[i], dp[i - coin[j]] + 1)

ans = dp[m]

if ans == INT_MAX:
    ans = -1

print(ans)