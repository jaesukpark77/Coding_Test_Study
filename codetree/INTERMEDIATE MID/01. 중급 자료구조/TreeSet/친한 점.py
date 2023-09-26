# problem link : https://www.codetree.ai/missions/8/problems/frendly-point?&utm_source=clipboard&utm_medium=text

from sortedcontainers import SortedSet

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]
queries = [tuple(map(int, input().split())) for _ in range(m)]

s = SortedSet(points)

for target in queries:
    idx = s.bisect_left(target)

    if idx == len(s):
        print(-1, -1)
    else:
        x, y = s[idx]
        print(x, y)