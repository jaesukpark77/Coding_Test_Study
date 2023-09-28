# problem link : https://www.codetree.ai/missions/8/problems/divide-evenly-2?&utm_source=clipboard&utm_medium=text

import math

INT_MAX = math.inf

MAX_R = 1000
MAX_Q = 4

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

ans = INT_MAX

points.sort()

for b in range(0, MAX_R + 1, 2):
    cnt = [0] * (MAX_Q + 1)

    for _, y in points:
        if y > b:
            cnt[1] += 1
        else:
            cnt[4] += 1

    for i in range(n):
        if i == 0 or points[i][0] != points[i - 1][0]:
            ans = min(ans, max(cnt))
    
        _, y = points[i]
        if y > b:
            cnt[1] -= 1
            cnt[2] += 1
        else:
            cnt[4] -= 1
            cnt[3] += 1

print(ans)