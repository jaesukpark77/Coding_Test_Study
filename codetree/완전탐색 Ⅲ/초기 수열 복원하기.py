# problem link : https://www.codetree.ai/missions/5/problems/restore-initial-sequence?&utm_source=clipboard&utm_medium=text

import sys

MAX_N = 1000

n = int(input())
a = list(map(int, input().split()))
arr = [0] * n

for i in range(1, n + 1):
    # 수열의 첫 번째 수가 i일 때
    arr[0] = i
    
    for j in range(1, n):
        arr[j] = a[j - 1] - arr[j - 1]

    satisfied = True
    exist = [False] * (MAX_N + 1)
    for j in range(n):
        if arr[j] <= 0 or arr[j] > n:
            satisfied = False
        else:
            if exist[arr[j]]:
                satisfied = False
            exist[arr[j]] = True

    if satisfied:
        for j in range(n):
            print(arr[j], end=" ")
        sys.exit()