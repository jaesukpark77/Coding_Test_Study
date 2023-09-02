# problem link : https://www.codetree.ai/missions/5/problems/create-consecutive-numbers-3?&utm_source=clipboard&utm_medium=text

import sys

a = list(map(int, input().split()))

a.sort()

if a[0] + 1 == a[1] and a[1] + 1 == a[2]:
    print(0)
    sys.exit()

max_move = 0

move = a[2] - a[1] - 1
max_move = max(max_move, move)

move = a[1] - a[0] - 1
max_move = max(max_move, move)

print(max_move)