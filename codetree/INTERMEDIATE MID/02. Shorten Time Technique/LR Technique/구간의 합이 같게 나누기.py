# problem link : https://www.codetree.ai/missions/8/problems/divide-by-equal-sum-of-intervals?&utm_source=clipboard&utm_medium=text

n = int(input())
arr = list(map(int ,input().split()))
L, R = [0] * n, [0] * n

total_sum = sum(arr)

if total_sum % 4 != 0:
    print(0)
    quit()

target_sum = total_sum // 4

L[0] = 0
sum_val = arr[0]
cnt = 1 if sum_val == target_sum else 0

for i in range(1, n):
    sum_val += arr[i]

    if sum_val == 2 * target_sum:
        L[i] = cnt

    if sum_val == target_sum:
        cnt += 1

R[n - 1] = 0
sum_val = arr[n-1]
cnt = 1 if sum_val == target_sum else 0

for i in range(n-2, -1, -1):
    sum_val += arr[i]

    if sum_val == 2 * target_sum:
        R[i] = cnt

    if sum_val == target_sum:
        cnt += 1

ans = 0

for i in range(1, n-1):
    ans += L[i] * R[i + 1]

print(ans)