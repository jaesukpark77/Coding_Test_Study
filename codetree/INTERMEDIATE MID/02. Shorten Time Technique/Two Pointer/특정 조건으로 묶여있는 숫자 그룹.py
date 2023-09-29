# problem link : https://www.codetree.ai/missions/8/problems/a-group-of-numbers-tied-to-specific-conditions?&utm_source=clipboard&utm_medium=text

n, k = map(int, input().split())
arr = [0] + [int(input()) for _ in range(n)]

L, R = [0] * (n + 1), [0] * (n + 1)

arr.sort()

max_sum = 0
i = 1
for j in range(1, n+1):
    while i + 1 <= j and arr[j] - arr[i] > k:
        i += 1
    
    max_sum = max(max_sum, j - i + 1)

    L[j] = max_sum

max_sum = 0
j = n
for i in range(n, 0, -1):
    while j - 1 >= i and arr[j] - arr[i] > k:
        j -= 1

    max_sum = max(max_sum, j - i + 1)

    R[i] = max_sum

ans = L[n]

for i in range(1, n):
    ans = max(ans, L[i] + R[i+1])

print(ans)