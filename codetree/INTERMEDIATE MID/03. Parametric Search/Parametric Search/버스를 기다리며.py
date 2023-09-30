# problem link : https://www.codetree.ai/missions/8/problems/waiting-for-the-bus?&utm_source=clipboard&utm_medium=text

n, m, c = map(int, input().split())
t = list(map(int, input().split()))

def is_possible(wait):
    bus = 1
    firstArrival = t[0]
    firstIndex = 0

    for i in range(n):
        if t[i] - firstArrival > wait or i + 1 - firstIndex > c:
            bus += 1
            firstArrival = t[i]
            firstIndex = i

    return bus <= m

t.sort()

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