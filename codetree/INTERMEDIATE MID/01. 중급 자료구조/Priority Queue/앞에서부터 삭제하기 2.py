# problem link : https://www.codetree.ai/missions/8/problems/delete-it-from-the-beginning-2?&utm_source=clipboard&utm_medium=text

import heapq

n = int(input())
arr = list(map(int, input().split()))

sum_val = 0
max_avg = 0
pq = []

heapq.heappush(pq, arr[n-1])
sum_val += arr[n-1]

for i in range(n-2, 0, -1):
    heapq.heappush(pq, arr[i])
    sum_val += arr[i]

    min_num = pq[0]
    avg = (sum_val - min_num) / (n - i - 1)

    if max_avg < avg:
        max_avg = avg

print(f'{max_avg:.2f}')