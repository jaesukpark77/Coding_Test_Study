# problem link : https://www.codetree.ai/missions/8/problems/section-with-maximum-overlap-2?&utm_source=clipboard&utm_medium=text

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0
points = []

for x1, x2 in segments:
    points.append((x1, +1))
    points.append((x2, -1))

points.sort()

sum_val = 0

for x, v in points:
    sum_val += v

    ans = max(ans, sum_val)

print(ans)