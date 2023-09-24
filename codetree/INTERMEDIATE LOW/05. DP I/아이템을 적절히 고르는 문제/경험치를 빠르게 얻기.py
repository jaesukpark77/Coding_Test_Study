# problem link : https://www.codetree.ai/missions/2/problems/gain-exp-quickly?&utm_source=clipboard&utm_medium=text

import math

INT_MIN = -math.inf
INT_MAX = math.inf

n, m = map(int, input().split())
exp_list, runtime_list =[0], [0]

for _ in range(n):
    exp, runtime = tuple(map(int, input().split()))
    exp_list.append(exp)
    runtime_list.append(runtime)

t = sum(runtime_list)
dp = [[0] * (t + 1) for _ in range(n + 1)]

def initailize():
    for i in range(n + 1):
        for j in range(t + 1):
            dp[i][j] = INT_MIN

    dp[0][0] = 0

initailize()

for i in range(1, n+1):
    for j in range(t+1):
        if j - runtime_list[i] >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - runtime_list[i]] + exp_list[i])

        dp[i][j] = max(dp[i][j], dp[i - 1][j])

ans = INT_MAX

for j in range(t+1):
    if dp[n][j] >= m:
        ans = min(ans, j)

if ans == INT_MAX:
    ans = -1

print(ans)