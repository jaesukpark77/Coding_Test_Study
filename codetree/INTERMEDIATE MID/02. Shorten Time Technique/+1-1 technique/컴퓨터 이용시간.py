# problem link : https://www.codetree.ai/missions/8/problems/computer-hours?&utm_source=clipboard&utm_medium=text

import heapq

n = int(input())

segments = [tuple(map(int, input().split())) for _ in range(n)]

assigned_nums = [0] * n

computers = []
for i in range(1, n+1):
    heapq.heappush(computers, i)

points = []
for i, (x1, x2) in enumerate(segments):
    points.append((x1, +1, i))
    points.append((x2, -1, i))

points.sort()

for x, v, index in points:
    if v == +1:
        computer_num = heapq.heappop(computers)

        assigned_nums[index] = computer_num
    else:
        computer_num = assigned_nums[index]
        heapq.heappush(computers, computer_num)

for num in assigned_nums:
    print(num, end=' ')