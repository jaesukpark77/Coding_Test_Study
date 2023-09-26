# problem link : https://www.codetree.ai/missions/8/problems/median?&utm_source=clipboard&utm_medium=text

import heapq

t = int(input())
arr = []

def find_median():
    median = arr[0]
    max_pq, min_pq = [], []
    print(median, end=' ')

    for i in range(1, m):
        if i % 2 == 1:
            if arr[i] < median:
                heapq.heappush(max_pq, -arr[i])
            else:
                heapq.heappush(min_pq, arr[i])
        else:
            if len(max_pq) > len(min_pq):
                new_card = -heapq.heappop(max_pq)
            else:
                new_card = heapq.heappop(min_pq)

            nums = sorted([median, arr[i], new_card])

            heapq.heappush(max_pq, -nums[0])
            median = nums[1]
            heapq.heappush(min_pq, nums[2])

            print(median, end=" ")

    print()

for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))

    find_median()