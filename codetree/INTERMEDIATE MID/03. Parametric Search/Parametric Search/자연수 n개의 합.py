# problem link : https://www.codetree.ai/missions/8/problems/sum-of-n-natural-numbers?&utm_source=clipboard&utm_medium=text

MAX_S = 10**9

s = int(input())
left = 1
right = MAX_S
max_num = 0

while left <= right:
    mid = (left + right) // 2
    if mid * (mid + 1) // 2 <= s:
        left = mid + 1
        max_num = max(max_num, mid)
    else:
        right = mid - 1

print(max_num)