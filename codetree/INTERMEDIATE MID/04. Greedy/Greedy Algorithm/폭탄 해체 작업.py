# problem link : https://www.codetree.ai/missions/8/problems/the-bomb-dismantling?&utm_source=clipboard&utm_medium=text

import heapq

MAX_T = 10000
n = int(input())
bombs = []
for _ in range(n):
    score, time_limit = tuple(map(int, input().split()))
    bombs.append((time_limit, score))

def get_time_limit(bomb_idx):
    time_limit, _ = bombs[bomb_idx]

    return time_limit

def get_score(bomb_idx):
    _, score = bombs[bomb_idx]
    
    return score

bombs.sort()

pq = []
bomb_idx = n - 1
ans = 0

for t in range(MAX_T, 0, -1):
    while bomb_idx >= 0 and get_time_limit(bomb_idx) >= t:
        heapq.heappush(pq, -get_score(bomb_idx))
        bomb_idx -=1

    if pq:
        ans += -heapq.heappop(pq)

print(ans)