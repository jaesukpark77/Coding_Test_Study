# problem link : https://www.codetree.ai/missions/2/problems/rod-cutting?&utm_source=clipboard&utm_medium=text

n = int(input())
profit = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)
dp[0] = 0

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + profit[j])

print(dp[n])