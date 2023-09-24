# problem link : https://www.codetree.ai/missions/2/problems/maximum-number-of-jumps?&utm_source=clipboard&utm_medium=text

import math

INT_MIN = -math.inf

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n

def initialize():
    for i in range(n):
        dp[i] = INT_MIN
        
    dp[0] = 0

initialize()

for i in range(1, n):
    for j in range(i):
        if dp[j] == INT_MIN:
            continue
        
        if j + arr[j] >= i:
            dp[i] = max(dp[i], dp[j] + 1)

ans = INT_MIN
for i in range(n):
    ans = max(ans, dp[i])

print(ans)