# problem link : https://www.codetree.ai/missions/8/problems/count-number-of-points-3?&utm_source=clipboard&utm_medium=text

from sortedcontainers import SortedSet

n, q = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

nums = SortedSet(arr)
mapper = dict()

cnt = 1

for num in nums:
    mapper[num] = cnt
    cnt += 1

for a, b in queries:
    new_a, new_b = mapper[a], mapper[b]
    print(new_b - new_a + 1)