# problem link : https://www.codetree.ai/missions/5/problems/study-cafe-keeping-distance-3?&utm_source=clipboard&utm_medium=text

import math
INT_MAX = math.inf

n = int(input())
seats = list(input())

max_dist = 0
max_i, max_j = -1, -1

for i in range(n):
    if seats[i] == '1':
        for j in range(i+1, n):
            if seats[j] == '1':
                if j - i > max_dist:
                    max_dist = j - i
                    max_i, max_j = i, j
                break

seats[(max_i + max_j) // 2] = '1'

ans = INT_MAX
for i in range(n):
    if seats[i] == '1':
        for j in range(i + 1, n):
            if seats[j] == '1':
                ans = min(ans, j - i)
                break

print(ans)