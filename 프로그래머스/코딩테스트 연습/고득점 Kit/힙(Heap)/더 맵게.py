# problem link : https://school.programmers.co.kr/learn/courses/30/lessons/42626

# heap method

import heapq

def solution(scoville, K):
    pq = []
    for s in scoville:
        heapq.heappush(pq, s)
    cnt = 0
    while pq[0] < K:
        heapq.heappush(pq, heapq.heappop(pq) + heapq.heappop(pq) * 2)
        cnt += 1
        
        if len(pq) == 1 and pq[0] < K:
            return -1
        
    return cnt

# deque method

from collections import deque

def solution(scoville, K):
    answer = 0
    d = deque()
    scoville.sort()
    sco = deque(scoville)
    
    while (sco and sco[0] < K) or (d and d[0] < K):
        answer += 1
        if len(sco) + len(d) <= 1:
            return -1
        
        food = [0] * 2
        for a in range(2):
            if sco and d:
                if sco[0] < d[0]:
                    food[a] = sco.popleft()
                else:
                    food[a] = d.popleft()
            elif sco:
                food[a] = sco.popleft()
            else:
                food[a] = d.popleft()
                
        d.append(food[0] + food[1] * 2)
    return answer