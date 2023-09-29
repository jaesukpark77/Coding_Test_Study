# problem link : https://www.codetree.ai/missions/8/problems/sum-closest-to-zero?&utm_source=clipboard&utm_medium=text

import math

INT_MAX = math.inf

n = int(input())
arr = list(map(int, input().split()))
arr = [0] + sorted(arr)

ans = INT_MAX

j = n
for i in range(1, n +1):
    if i < j:
        ans = min(ans, abs(arr[i] + arr[j]))

    while i < j - 1 and arr[i] + arr[j] > 0:
        j -= 1
        ans = min(ans, abs(arr[i] + arr[j]))

print(ans)