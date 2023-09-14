# problem link : https://www.codetree.ai/missions/5/problems/study-cafe-keeping-distance-2?&utm_source=clipboard&utm_medium=text

import math

INT_MAX = math.inf

n = int(input())
seats = list(input())

max_dist = 0
max_i, max_j = -1, -1
for i in range(n):
    if seats[i] == '1':
        for j in range(i + 1, n):
            if seats[j] == '1':
                if j - i > max_dist:
                    max_dist = j - i
                    max_i, max_j = i, j
                break

max_dist2 = -1
max_idx = -1

if seats[0] == '0':
    dist = 0
    for i in range(1, n):
        if seats[i] == '1':
            break
        dist += 1

    if dist > max_dist2:
        max_dist2 = dist
        max_idx = 0

if seats[n - 1] == '0':
    dist = 0
    for i in range(n - 2, -1, -1):
        if seats[i] == '1':
            break
        dist += 1

    if dist > max_dist2:
        max_dist2 = dist
        max_idx = n - 1

if max_dist2 >= max_dist // 2:
    seats[max_idx] = '1'
else:
    seats[(max_i + max_j) // 2] = '1'

ans = INT_MAX
for i in range(n):
    if seats[i] == '1':
        for j in range(i + 1, n):
            if seats[j] == '1':
                ans = min(ans, j - i)
                break

print(ans)