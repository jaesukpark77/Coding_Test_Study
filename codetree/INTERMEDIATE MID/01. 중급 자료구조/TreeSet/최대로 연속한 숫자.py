# problem link : https://www.codetree.ai/missions/8/problems/maximum-consecutive-number?&utm_source=clipboard&utm_medium=text

from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = list(map(int, input().split()))
s_num = SortedSet()
s_len = SortedSet()

s_num.add(-1)
s_num.add(n+1)
s_len.add((-(n+1), -1, n+1))

for y in arr:
    s_num.add(y)

    z = s_num[s_num.bisect_right(y)]
    x = s_num[s_num.bisect_left(y) - 1]

    s_len.remove((-(z - x - 1), x, z))
    s_len.add((-(y - x - 1), x, y))
    s_len.add((-(z - y - 1), y, z))

    best_length, _, _ = s_len[0]
    print(-best_length)