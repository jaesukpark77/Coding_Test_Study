# problem link : https://www.codetree.ai/missions/8/problems/taking-a-taxi-in-the-middle-of-the-marathon?&utm_source=clipboard&utm_medium=text

import math

INT_MAX = math.inf

n = int(input())
x, y = [], []

L, R = [0] * n, [0] * n
ans = INT_MAX

for _ in range(n):
    given_x, given_y = tuple(map(int, input().split()))
    x.append(given_x)
    y.append(given_y)

L[0] = 0
for i in range(1, n):
    L[i] = L[i-1] + abs(x[i] - x[i-1]) + abs(y[i] - y[i-1])

R[n-1] = 0
for i in range(n-2, -1, -1):
    R[i] = R[i + 1] + abs(x[i + 1] - x[i]) + abs(y[i + 1] - y[i])

for i in range(1, n-1):
    ans = min(ans, L[i-1] + R[i+1] + abs(x[i+1] - x[i-1]) + abs(y[i+1] - y[i-1]))

print(ans)