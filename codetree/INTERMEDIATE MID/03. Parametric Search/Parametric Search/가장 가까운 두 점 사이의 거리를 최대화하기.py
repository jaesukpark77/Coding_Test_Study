# problem link : https://www.codetree.ai/missions/8/problems/maximize-dist-of-nearest-points?&utm_source=clipboard&utm_medium=text

n = int(input())
segments = [list(map(int, input().split())) for _ in range(n)]
segments.sort()

def is_possible(mid):
    curr_x, _ = segments[0]
    for x1, x2 in segments[1:]:
        if x2 < curr_x + mid:
            return False
        curr_x = max(curr_x + mid, x1)
    
    return True

lo = 1
hi = 10**9
ans = 0

while lo <= hi:
    mid = (lo + hi) // 2

    if is_possible(mid):
        lo = mid + 1
        ans = max(ans, mid)
    else:
        hi = mid - 1

print(ans)