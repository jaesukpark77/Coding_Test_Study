# problem link : https://www.codetree.ai/missions/2/problems/minimum-diff-partition?&utm_source=clipboard&utm_medium=text

import math

INT_MAX = math.inf

n = int(input())
arr = [0] + list(map(int, input().split()))

m = sum(arr)
dp = [[0] * (m+1) for _ in range(n+1)]

def initialize():
    dp[0][0] = True

initialize()

for i in range(1, n+1):
    for j in range(m+1):
        if j >= arr[i] and dp[i-1][j - arr[i]]:
            dp[i][j] = True
        
        if dp[i-1][j]:
            dp[i][j] = True

ans = INT_MAX
for i in range(1, m):
    if dp[n][i]:
        ans = min(ans, abs(i - (m - i)))

print(ans)