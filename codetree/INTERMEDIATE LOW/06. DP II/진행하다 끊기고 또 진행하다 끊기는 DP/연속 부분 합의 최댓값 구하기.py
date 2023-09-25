# problem link : https://www.codetree.ai/missions/2/problems/max-of-partial-sum?&utm_source=clipboard&utm_medium=text

import math

INT_MIN = -math.inf

n = int(input())
a = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)

def initialize():
    for i in range(n+1):
        dp[i] = INT_MIN

    dp[1] = a[1]

initialize()

for i in range(2, n+1):
    dp[i] = max(dp[i -1] + a[i], a[i])

ans = max(dp[1:n+1])

print(ans)