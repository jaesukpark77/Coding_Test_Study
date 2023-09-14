# problem link : https://www.codetree.ai/missions/5/problems/multiply-two-and-remove-one-number?&utm_source=clipboard&utm_medium=text

import sys

INT_MAX = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

def score(removed_idx):
    sum_val = 0

    prev = -1

    for i in range(n):
        if i == removed_idx:
            continue
        if prev != -1:
            sum_val += abs(arr[i] - prev)

        prev = arr[i]

    return sum_val

min_score = INT_MAX

for i in range(n):
    arr[i] *= 2

    for j in range(n):
        min_score = min(min_score, score(j))

    arr[i] //= 2

print(min_score)