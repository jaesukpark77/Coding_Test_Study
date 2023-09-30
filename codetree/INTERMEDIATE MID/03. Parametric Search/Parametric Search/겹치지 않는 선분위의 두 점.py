# problem link : https://www.codetree.ai/missions/8/problems/two-points-of-the-line-that-don't-overlap?&utm_source=clipboard&utm_medium=text

MAX_NUM = 10**18

n, m = map(int, input().split())
segments = [tuple(map(int, input().split())) for _ in range(m)]

def is_possible(dist):
    cnt = 0
    last_x = -MAX_NUM

    for a, b in segments:
        while last_x + dist <= b:
            cnt += 1
            last_x = max(a, last_x + dist)

            if cnt >= n:
                break

    return cnt >= n

segments.sort()

left = -1
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