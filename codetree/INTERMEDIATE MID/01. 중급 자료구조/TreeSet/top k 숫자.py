# problem link : https://www.codetree.ai/missions/8/problems/top-k-elements?&utm_source=clipboard&utm_medium=text

from sortedcontainers import SortedSet

n, k = map(int, input().split())
arr = list(map(int, input().split()))

s = SortedSet()

for x in arr:
    s.add(-x)

for i in range(k):
    print(-s[i], end=' ')