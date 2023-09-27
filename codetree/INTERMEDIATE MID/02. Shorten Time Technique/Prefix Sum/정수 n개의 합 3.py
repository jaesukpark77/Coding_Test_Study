# problem link : https://www.codetree.ai/missions/8/problems/sum-of-n-integers-3?&utm_source=clipboard&utm_medium=text

import math

INT_MIN = -math.inf

n, k = map(int, input().split())
arr = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
prefix_sum = [[0] * (n+1) for _ in range(n+1)]
ans = INT_MIN

def get_sum(x1, y1, x2, y2):
    return prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1]

prefix_sum[0][0] = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + arr[i][j]

for i in range(1, n - k + 2):
    for j in range(1, n - k + 2):
        ans = max(ans, get_sum(i, j, i + k - 1, j + k - 1))

print(ans)