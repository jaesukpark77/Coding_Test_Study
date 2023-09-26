# problem link : https://www.codetree.ai/missions/8/problems/sum-of-n-integers-2?&utm_source=clipboard&utm_medium=text

import math

INT_MIN = -math.inf

n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
prefix_sum = [0] * (n + 1)
ans = INT_MIN

def get_sum(s, e):
    return prefix_sum[e] - prefix_sum[s - 1]

prefix_sum[0] = 0

for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

for i in range(1, n - k + 2):
    ans = max(ans, get_sum(i, i + k -1))

print(ans)