# problem link : https://www.codetree.ai/missions/5/problems/maximum-h-score-2?&utm_source=clipboard&utm_medium=text

n, l = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(1, n+1):
    cnt = 0
    cnt1 = 0

    for j in range(n):
        if a[j] >= i:
            cnt += 1
        elif a[j] == i - 1:
            if cnt1 < l:
                cnt1 += 1
                cnt += 1

    if cnt >= i:
        ans = i

print(ans)