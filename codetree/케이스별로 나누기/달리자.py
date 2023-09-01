# problem link : https://www.codetree.ai/missions/5/problems/run-and-run?&utm_source=clipboard&utm_medium=text

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0

for i in range(n):
    if a[i] > b[i]:
        num = a[i] - b[i]
        a[i] -= num
        a[i + 1] += num
        ans += num

print(ans)