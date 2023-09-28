# problem link : https://www.codetree.ai/missions/8/problems/remove-the-line-segment-for-the-maximum-length?&utm_source=clipboard&utm_medium=text

import math

INT_MAX = math.inf

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

weights = [0] * n

points = []
for i in range(n):
    x1, x2 = segments[i]
    points.append((x1, +1, i))
    points.append((x2, -1, i))

points.sort()

tot_length = 0
segs = set()
prev_x= -1

for x, v, index in points:
    seg_cnt = len(segs)

    if seg_cnt > 0:
        tot_length += x - prev_x

    if seg_cnt == 1:
        target_index = list(segs)[0]
        weights[target_index] += x - prev_x

    if v == +1:
        segs.add(index)

    else:
        segs.remove(index)

    prev_x = x

min_length = INT_MAX
for i in range(n):
    min_length = min(min_length, weights[i])

print(tot_length - min_length)