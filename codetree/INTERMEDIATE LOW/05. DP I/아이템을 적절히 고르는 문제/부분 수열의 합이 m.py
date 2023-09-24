# problem link : https://www.codetree.ai/missions/2/problems/the-sum-of-the-subsequences-is-m?&utm_source=clipboard&utm_medium=text

MAX_ANS = 101

n, m = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0] * (m + 1)

def initialize():
    for i in range(m+1):
        dp[i] = MAX_ANS
    
    dp[0] = 0

initialize()

for i in range(n):
    for j in range(m, -1, -1):
        if j >= arr[i]:
            dp[j] = min(dp[j], dp[j - arr[i]] + 1)

min_len = dp[m]

if min_len == MAX_ANS:
    min_len = -1

print(min_len)