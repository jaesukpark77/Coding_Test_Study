# problem link : https://www.codetree.ai/missions/9/problems/calculating-an-integer-for-a-node?&utm_source=clipboard&utm_medium=text

import sys
sys.setrecursionlimit(100000)

n = int(input())
edges = [[] for _ in range(n + 1)]

arr = [0] * (n + 1)
dp = [0] * (n + 1)

for i in range(2, n + 1):
    t, a, p = tuple(map(int, input().split()))
    edges[p].append(i)

    arr[i] = a if t == 1 else -a

def dfs(x):
    for y in edges[x]:
        dfs(y)

    dp[x] = arr[x]
    for y in edges[x]:
        if dp[y] > 0:
            dp[x] += dp[y]

dfs(1)

print(dp[1])