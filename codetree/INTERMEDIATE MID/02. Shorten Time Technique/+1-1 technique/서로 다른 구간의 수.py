# problem link : https://www.codetree.ai/missions/8/problems/number-of-distinct-segments?&utm_source=clipboard&utm_medium=text

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

points = []
for i, (x1, x2) in enumerate(segments):
    points.append((x1, +1, i))
    points.append((x2, -1, i))

points.sort()

segs = set()
ans = 0

for x, v, index in points:
    if v == +1:
        if not segs:
            ans += 1
        
        segs.add(index)
    else:
        segs.remove(index)

print(ans)