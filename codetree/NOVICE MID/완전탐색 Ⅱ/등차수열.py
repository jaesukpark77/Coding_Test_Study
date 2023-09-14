# problem link : https://www.codetree.ai/missions/5/problems/arithmetic-sequence?utm_source=clipboard&utm_medium=text

MAX_A = 100

n = int(input())

arr = list(map(int, input().split()))

ans = 0
for x in range(1, MAX_A+1):
    cnt = 0

    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == x * 2:
                cnt += 1
    ans = max(ans, cnt)

print(ans)