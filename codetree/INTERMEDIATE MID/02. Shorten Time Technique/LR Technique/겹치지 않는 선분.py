# problem link : https://www.codetree.ai/missions/8/problems/line-segments-that-do-not-overlap?&utm_source=clipboard&utm_medium=text

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
L, R = [0] * n, [0] * n

segments.sort()

_, x2 = segments[0]
L[0] = x2

for i in range(1, n):
    _, x2 = segments[i]
    L[i] = max(L[i-1], x2)

_, x2 = segments[n-1]
R[n-1] = x2

for i in range(n-2, -1, -1):
    _, x2 = segments[i]
    R[i] = min(R[i+1], x2)

ans = 0

for i in range(n):
    _, x2 = segments[i]

    if i > 0 and L[i - 1] >= x2:
        continue
    
    if i < n - 1 and R[i+1] <= x2:
        continue

    ans += 1

print(ans)