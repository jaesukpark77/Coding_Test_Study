# problem link : https://www.codetree.ai/missions/8/problems/array-extraction?&utm_source=clipboard&utm_medium=text

import heapq

n = int(input())
arr = [int(input()) for _ in range(n)]

pq = []

for x in arr:
    if x != 0:
        heapq.heappush(pq, -x)
    else:
        if not pq:
            print(0)
        else:
            print(-heapq.heappop(pq))