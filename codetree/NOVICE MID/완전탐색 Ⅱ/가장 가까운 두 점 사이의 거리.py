import math
INT_MAX = math.inf

n = int(input())

points = [tuple(map(int ,input(). split())) for _ in range(n)]

def dist(i, j):
    x1, y1 = points[i]
    x2, y2 = points[j]

    return (x1 - x2)**2 + (y1 - y2)**2

min_dist = INT_MAX
for i in range(n):
    for j in range(i+1, n):
        min_dist = min(min_dist, dist(i, j))

print(min_dist)