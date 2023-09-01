# problem link : https://www.codetree.ai/missions/5/problems/overlapping-line-segments?&utm_source=clipboard&utm_medium=text

import math

INT_MAX = math.inf

n = int(input())

max_x1 = 0
min_x2 = INT_MAX

for _ in range(n):
    x1, x2 = map(int, input().split())
    max_x1 = max(max_x1, x1)
    min_x2 = min(min_x2, x2)

if min_x2 >= max_x1:
    print("Yes")
else:
    print("No")