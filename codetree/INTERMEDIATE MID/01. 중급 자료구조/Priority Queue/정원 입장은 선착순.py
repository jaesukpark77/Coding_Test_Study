# problem link : https://www.codetree.ai/missions/8/problems/admission-to-the-garden-is-on-a-first-come-first-served-basis?&utm_source=clipboard&utm_medium=text

import heapq
import math

INT_MAX = math.inf

n = int(input())

ans = 0
pq = []

people = []
for i in range(n):
    a, t = tuple(map(int, input().split()))

    people.append((a, i + 1, t))

people.append((INT_MAX, n + 1, 0))
people.sort()

exist_time = 0

for a, num, t in people:
    while a>= exist_time and pq:
        _, next_a, next_t = heapq.heappop(pq)

        ans = max(ans, exist_time - next_a)
        exist_time += next_t

    if a >= exist_time:
        exist_time = a + t
    else:
        heapq.heappush(pq, (num, a, t))

print(ans)