# problem link : https://www.codetree.ai/missions/8/problems/find-maximum-number?&utm_source=clipboard&utm_medium=text

from sortedcontainers import SortedSet

n, m = map(int, input().split())
queries = list(map(int, input().split()))

s = SortedSet(range(1, m+1))

for target in queries:
    s.remove(target)

    print(s[-1])