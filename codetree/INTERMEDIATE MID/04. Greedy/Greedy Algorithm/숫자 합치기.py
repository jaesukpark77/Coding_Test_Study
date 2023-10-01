# problem link : https://www.codetree.ai/missions/8/problems/%08merge-numbers?&utm_source=clipboard&utm_medium=text

import heapq

n = int(input())
arr = list(map(int, input().split()))

pq = []
ans = 0

for elem in arr:
    heapq.heappush(pq, elem)

while len(pq) > 1:
    x1 = heapq.heappop(pq)
    x2 = heapq.heappop(pq)

    ans += (x1 + x2)
    heapq.heappush(pq, x1 + x2)

print(ans)