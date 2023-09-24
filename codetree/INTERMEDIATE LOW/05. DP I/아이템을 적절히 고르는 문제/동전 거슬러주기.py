# problem link : https://www.codetree.ai/missions/2/problems/coin-change?&utm_source=clipboard&utm_medium=text

# DP - Tabulation Method

MAX_ANS = 10001

n, m = map(int, input().split())
coin = [0] + list(map(int, input().split()))
dp = [MAX_ANS for _ in range(m + 1)]

dp[0] = 0

for i in range(1, m+1):
    for j in range(1, n+1):
        if i >= coin[j]:
            dp[i] = min(dp[i], dp[i - coin[j]] + 1)

min_cnt = dp[m]

if min_cnt == MAX_ANS:
    min_cnt = -1

print(min_cnt)

# BFS Method

from collections import deque

n, m = map(int ,input().split())
coin = [0] + list(map(int, input().split()))

q = deque()

visited = [False for _ in range(m+1)]
step = [0 for _ in range(m+1)]
ans = 0

def in_range(num):
    return num <= m

def can_go(num):
    return in_range(num) and not visited[num]

def push(num, new_step):
    q.append(num)
    visited[num] = True
    step[num] = new_step

def find_min():
    global ans

    while q:
        curr_num = q.popleft()

        for i in range(1, n+1):
            if can_go(curr_num + coin[i]):
                push(curr_num + coin[i], step[curr_num] + 1)

    if visited[m]:
        ans = step[m]
    else:
        ans = -1

push(0, 0)
find_min()
print(ans)