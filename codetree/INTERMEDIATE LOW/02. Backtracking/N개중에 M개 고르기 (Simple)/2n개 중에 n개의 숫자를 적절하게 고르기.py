# problem link : https://www.codetree.ai/missions/2/problems/choose-n-out-of-2n-properly?&utm_source=clipboard&utm_medium=text

import math

INT_MAX = math.inf

n = int(input())
num = list(map(int, input().split()))
visited = [False for _ in range(2 * n)]

ans = INT_MAX

def calc():
    diff = 0
    for i in range(2*n):
        diff = (diff + num[i]) if visited[i] else diff - num[i]
    
    return abs(diff)

def find_min(idx, cnt):
    global ans

    if cnt == n:
        ans = min(ans, calc())
        return
    
    if idx == 2 * n:
        return
    
    visited[idx] = True
    find_min(idx + 1, cnt + 1)
    visited[idx] = False

    find_min(idx + 1, cnt)

find_min(0, 0)
print(ans)