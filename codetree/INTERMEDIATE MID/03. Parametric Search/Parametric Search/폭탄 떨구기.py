# problem link : https://www.codetree.ai/missions/8/problems/drop-the-bomb?&utm_source=clipboard&utm_medium=text

n, k = map(int, input().split())
pos = [int(input()) for _ in range(n)]

def is_possible(mid):
    cnt = 1
    idx = 0

    for i in range(n):
        if pos[i] - pos[idx] <= 2 * mid:
            continue
        else:
            cnt += 1
            idx = i
    
    return cnt <= k

pos.sort()

lo = 0
hi = 10**9
ans = 10**9

while lo <= hi:
    mid = (lo + hi) // 2
    if is_possible(mid):
        hi = mid - 1
        ans = min(ans, mid)
    else:
        lo = mid + 1

print(ans)