# problem link : https://www.codetree.ai/missions/8/problems/maximum-distance-point?&utm_source=clipboard&utm_medium=text

MAX_NUM = 10**9

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

def is_possible(dist):
    cnt = 1
    last_idx = 0
    for i in range(1, n):
        if arr[i] - arr[last_idx] >= dist:
            cnt += 1
            last_idx = i

    return cnt >= m

arr.sort()

left = 1
right = MAX_NUM
ans = 0

while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        left = mid + 1
        ans = max(ans, mid)
    else:
        right = mid - 1

print(ans)