# problem link : https://www.codetree.ai/missions/8/problems/implement-fractional-knapsack?&utm_source=clipboard&utm_medium=text

n, m = map(int, input().split())
jewls = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0

jewls.sort(key = lambda x: -x[1] / x[0])

for w, v in jewls:
    if m >= w:
        m -= w
        ans += v
    else:
        ans += m / w * v
        break

print(f'{ans:.3f}')