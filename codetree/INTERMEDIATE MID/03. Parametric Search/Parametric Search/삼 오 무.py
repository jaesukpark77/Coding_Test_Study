# problem link : https://www.codetree.ai/missions/8/problems/distributing-integers?&utm_source=clipboard&utm_medium=text

import sys

INT_MAX = sys.maxsize

n = int(input())

def get_num_of_numbers(mid):
    moo_cnt = mid // 3 + mid // 5 - mid // 15

    return mid - moo_cnt

left = 1
right = INT_MAX
min_num = INT_MAX

while left <= right:
    mid = (left + right) // 2
    if get_num_of_numbers(mid) >= n:
        right = mid - 1
        min_num = min(min_num, mid)
    else:
        left = mid + 1

print(min_num)