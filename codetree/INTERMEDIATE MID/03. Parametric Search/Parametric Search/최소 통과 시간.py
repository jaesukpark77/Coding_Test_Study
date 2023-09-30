# problem link : https://www.codetree.ai/missions/8/problems/minimum-transit-time?&utm_source=clipboard&utm_medium=text

MAX_NUM = 10**14

n, m = map(int, input().split())
arr = [int(input()) for _ in range(m)]

def is_possible(transit_time):
    cnt = 0
    for i in range(m):
        cnt += transit_time // arr[i]

    return cnt >= n

left = 1
right = MAX_NUM
ans = MAX_NUM

while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1

print(ans)