# problem link : https://www.codetree.ai/missions/5/problems/teleportation?&utm_source=clipboard&utm_medium=text

import math

INT_MAX = math.inf

a, b, x, y = map(int, input().split())

min_dist = INT_MAX

min_dist = min(min_dist, abs(b - a))
min_dist = min(min_dist, abs(x - a) + abs(b - y))
min_dist = min(min_dist, abs(y - a) + abs(b - x))

print(min_dist)