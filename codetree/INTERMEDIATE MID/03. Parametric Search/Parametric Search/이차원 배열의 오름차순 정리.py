# problem link : https://www.codetree.ai/missions/8/problems/ascending-order-of-two-dimensional-array?&utm_source=clipboard&utm_medium=text

n = int(input())
k = int(input())

lo = 1
hi = n * n
ans = n * n

while lo <= hi:
    mid = (lo + hi) // 2

    val = 0
    for i in range(1, n+1):
        val += min(n, mid // i)

    if val >= k:
        hi = mid - 1
        ans = min(ans, mid)
    else:
        lo = mid + 1

print(ans)