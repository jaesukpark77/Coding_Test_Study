# problem link : https://www.codetree.ai/missions/8/problems/find-number-fast-2?&utm_source=clipboard&utm_medium=text

from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

s = SortedSet(arr)

for num in queries:
    idx = s.bisect_left(num)

    if idx == len(s):
        print(-1)
    else:
        print(s[idx])