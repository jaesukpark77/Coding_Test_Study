# problem link : https://www.codetree.ai/missions/8/problems/both-exist-section?&utm_source=clipboard&utm_medium=text

import math

INT_MAX = math.inf

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

count_array_in = [0] * (m + 1)
count_array_out = [0] * (m + 1)

distinct_num_in = 0
distinct_num_out = 0

def push(idx):
    global distinct_num_in, distinct_num_out
    num = arr[idx]

    if count_array_in[num] == 0:
        distinct_num_in += 1
    
    count_array_in[num] += 1

    count_array_out[num] -= 1

    if count_array_out[num] == 0:
        distinct_num_out -= 1

def pop(idx):
    global distinct_num_in, distinct_num_out
    num = arr[idx]

    count_array_in[num] -= 1
    if count_array_in[num] == 0:
        distinct_num_in -= 1
    
    if count_array_out[num] == 0:
        distinct_num_out += 1
    
    count_array_out[num] += 1

for i in range(1, n+1):
    if count_array_out[arr[i]] == 0:
        distinct_num_out += 1

    count_array_out[arr[i]] += 1

ans = INT_MAX

j = 0 
for i in range(1, n+1):
    while j + 1 <= n and distinct_num_in < m:
        push(j+1)
        j += 1

    if distinct_num_in < m:
        break

    if distinct_num_out == m:
        ans = min(ans, j - i + 1)

    pop(i)

if ans == INT_MAX:
    ans = -1

print(ans)