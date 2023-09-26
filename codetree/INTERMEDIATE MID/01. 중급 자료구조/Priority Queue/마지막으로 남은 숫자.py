# problem link : https://www.codetree.ai/missions/8/problems/last-remaining-number?&utm_source=clipboard&utm_medium=text

import heapq

n = int(input())
arr = list(map(int, input().split()))

pq = []

for elem in arr:
    heapq.heappush(pq, -elem)

while (len(pq) >= 2):
    x = -heapq.heappop(pq)
    y = -heapq.heappop(pq)

    diff = x - y
    if diff != 0:
        heapq.heappush(pq, -diff)

if len(pq) == 1:
    print(-heapq.heappop(pq))
else:
    print(-1)