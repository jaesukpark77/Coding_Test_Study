# problem link : https://www.codetree.ai/missions/8/problems/meet-now-right-now?&utm_source=clipboard&utm_medium=text

n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))

def is_possible(time):
    max_x1 = x[0] - v[0] * time
    min_x2 = x[0] + v[0] * time

    for i in range(1, n):
        x1 = x[i] - v[i] * time
        x2 = x[i] + v[i] * time

        max_x1 = max(max_x1, x1)

        min_x2 = min(min_x2, x2)

    return max_x1 <= min_x2

lo = 0
hi = 1e9
ans = 1e9

for _ in range(100):
    mid = (lo + hi) / 2
    if is_possible(mid):
        hi = mid
        ans = min(ans, mid)
    else:
        lo = mid

print(f'{ans:.4f}')