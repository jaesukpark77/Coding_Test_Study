# problem link : n, k = map(int, input().split())
ans = 0

x = 0
segments = []

for _ in range(n):
    dist, c_dir = tuple(input().split())
    dist = int(dist)

    if c_dir == 'L':
        segments.append((x - dist, x))
        x -= dist
    else:
        segments.append((x, x + dist))
        x += dist

points = []

for x1, x2 in segments:
    points.append((x1, +1))
    points.append((x2, -1))

points.sort()

sum_val = 0

for i, (x, v) in enumerate(points):
    if sum_val >= k:
        prev_x, _ = points[i - 1]
        ans += x - prev_x

    sum_val += v

print(ans)

n, k = map(int, input().split())
ans = 0

x = 0
segments = []

for _ in range(n):
    dist, c_dir = tuple(input().split())
    dist = int(dist)

    if c_dir == 'L':
        segments.append((x - dist, x))
        x -= dist
    else:
        segments.append((x, x + dist))
        x += dist

points = []

for x1, x2 in segments:
    points.append((x1, +1))
    points.append((x2, -1))

points.sort()

sum_val = 0

for i, (x, v) in enumerate(points):
    if sum_val >= k:
        prev_x, _ = points[i - 1]
        ans += x - prev_x

    sum_val += v

print(ans)