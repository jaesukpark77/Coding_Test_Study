# problem link : https://www.codetree.ai/missions/2/problems/1-2-5-plus?&utm_source=clipboard&utm_medium=text

MAX_M = 3
MOD = 10007

n = int(input())
dp = [0] * (n+1)
numbers = [1, 2, 5]

dp[0] = 1

for i in range(1, n+1):
    for j in range(MAX_M):
        if i >= numbers[j]:
            dp[i] = (dp[i] + dp[i - numbers[j]]) % MOD

print(dp[n])