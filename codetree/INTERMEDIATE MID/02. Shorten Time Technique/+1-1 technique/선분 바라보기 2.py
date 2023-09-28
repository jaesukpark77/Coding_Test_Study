# problem link : https://www.codetree.ai/missions/8/problems/looking-at-the-line-segment-2?&utm_source=clipboard&utm_medium=text

from sortedcontainers import SortedSet

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

visible = [False] * n

points = []
for i in range(n):
    y, x1, x2 = segments[i]
    points.append((x1, +1, i, y))
    points.append((x2, -1, i, y))

points.sort()

segs = SortedSet()
for _, v, index, y in points:
    if v == +1:
        segs.add((y, index))
    else:
        segs.remove((y, index))
    
    if not segs:
        continue

    _, target_index = segs[0]
    visible[target_index] = True

ans = 0
for i in range(n):
    if visible[i]:
        ans += 1

print(ans)