# problem link : https://www.codetree.ai/missions/8/problems/sum-of-kth-smallest-pair?&utm_source=clipboard&utm_medium=text

import heapq

n, m, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

pq = []

arr1.sort()
arr2.sort()

for i in range(n):
    heapq.heappush(pq, (arr1[i] + arr2[0], i, 0))

for i in range(k - 1):
    _, idx1, idx2 = heapq.heappop(pq)

    idx2 += 1
    if idx2 < m:
        heapq.heappush(pq, (arr1[idx1] + arr2[idx2], idx1, idx2))

pair_sum, _, _ = heapq.heappop(pq)

print(pair_sum)