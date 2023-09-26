# problem link : https://www.codetree.ai/missions/8/problems/take-place?&utm_source=clipboard&utm_medium=text

from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = list(map(int, input().split()))

seats = SortedSet(range(1, m + 1))

ans = 0

for elem in arr:
    idx = seats.bisect_right(elem)

    if idx != 0:
        idx -= 1
        seats.remove(seats[idx])

        ans += 1
    else:
        break

print(ans)