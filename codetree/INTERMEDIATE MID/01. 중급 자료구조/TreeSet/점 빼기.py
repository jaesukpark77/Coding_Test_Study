# problem link : https://www.codetree.ai/missions/8/problems/remove-point?&utm_source=clipboard&utm_medium=text

from sortedcontainers import SortedSet

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

s = SortedSet(points)

for _ in range(m):
    k = int(input())

    idx = s.bisect_right((k, -1))

    if idx == len(s):
        print('-1 -1')
    else:
        x, y = s[idx]
        print(x, y)
        s.remove(s[idx])