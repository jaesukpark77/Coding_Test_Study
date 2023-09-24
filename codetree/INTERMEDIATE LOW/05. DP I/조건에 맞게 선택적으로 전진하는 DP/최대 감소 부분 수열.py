# problem link : https://www.codetree.ai/missions/2/problems/longest-decreasing-subsequence?&utm_source=clipboard&utm_medium=text

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    dp[i] = 1

    for j in range(i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

ans = 0

for i in range(n):
    ans = max(ans, dp[i])

print(ans)