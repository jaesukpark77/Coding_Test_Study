# problem link : https://www.codetree.ai/missions/8/problems/three-non-adjacent-numbers?&utm_source=clipboard&utm_medium=text

n = int(input())
arr = list(map(int, input().split()))
L, R =[0] * n, [0] * n

ans = 0

L[0] = arr[0]
for i in range(1, n):
    L[i] = max(L[i-1], arr[i])

R[n-1] = arr[n-1]
for i in range(n-2, -1, -1):
    R[i] = max(R[i+1], arr[i])

for i in range(2, n-2):
    ans = max(ans, L[i-2] + arr[i] + R[i+2])

print(ans)