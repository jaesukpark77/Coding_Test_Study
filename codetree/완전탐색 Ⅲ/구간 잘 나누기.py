# problem link : https://www.codetree.ai/missions/5/problems/divide-sections-well?&utm_source=clipboard&utm_medium=text

MAX_A = 10000

n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = MAX_A
for i in range(1, MAX_A + 1):
    possible = True
    section = 1

    cnt = 0
    for j in range(n):
        if arr[j] > i:
            possible = False
            break

        if cnt + arr[j] > i:
            cnt = 0
            section += 1

        cnt += arr[j]

    if possible and section <= m:
        ans = min(ans, i)

print(ans)