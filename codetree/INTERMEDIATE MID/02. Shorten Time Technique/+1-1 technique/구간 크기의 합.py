# problem link : https://www.codetree.ai/missions/8/problems/sum-of-interval-sizes?&utm_source=clipboard&utm_medium=text

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

points = []
for i, (x1, x2) in enumerate(segments):
    points.append((x1, +1, i))
    points.append((x2, -1, i))

points.sort()

segs = set()

ans = 0
start_x = -1

for x, v, index in points:
    if v == +1:
        if not segs:
            start_x = x
        segs.add(index)
    else:
        segs.remove(index)

        if not segs:
            end_x = x
            ans += end_x - start_x

print(ans)