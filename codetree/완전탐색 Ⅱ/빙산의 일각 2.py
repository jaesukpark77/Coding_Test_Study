# problem link : https://www.codetree.ai/missions/5/problems/the-tip-of-the-iceberg-2?utm_source=clipboard&utm_medium=text

MAX_H = 100

n = int(input())

h = [int(input()) for _ in range(n)]

ans = 0

for i in range(1, MAX_H + 1):
    cnt = 0
    if h[0] > i:
        cnt += 1

    for j in range(1, n):
        if h[j] > i and h[j - 1] <= i:
            cnt += 1
    
    ans = max(ans, cnt)

print(ans)