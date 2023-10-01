# problem link : https://www.codetree.ai/missions/8/problems/add-coins?&utm_source=clipboard&utm_medium=text

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

ans = 0

for coin in coins[::-1]:
    ans += k // coin
    k %= coin

print(ans)