# problem link : https://www.codetree.ai/missions/8/problems/nearest-number?&utm_source=clipboard&utm_medium=text

from sortedcontainers import SortedSet
import math

INT_MAX = math.inf

n = int(input())
queries = list(map(int, input().split()))

s = SortedSet()
ans = INT_MAX

s.add(0)

for x in queries:
    idx = s.bisect_right(x)

    if idx != len(s):
        ans = min(ans, s[idx] - x)

    idx -= 1

    ans = min(ans, x - s[idx])

    s.add(x)
    print(ans)