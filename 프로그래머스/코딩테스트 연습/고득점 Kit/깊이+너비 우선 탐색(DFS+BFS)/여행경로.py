# problem link : https://school.programmers.co.kr/learn/courses/30/lessons/43164

from collections import deque

def solution(tickets):
    answer = []
    tickets.sort(key = lambda x: (x[0], x[1]))
    q = deque([(["ICN"], tickets)])
    
    while q:
        now_path, now_t = q.popleft()
        
        if len(now_t) == 0:
            answer = now_path
            break
        
        valid_idx = -1
        
        for i in range(len(now_t)):
            if now_t[i][0] == now_path[-1]:
                valid_idx = i
                break
                
        if valid_idx == -1:
            continue
        
        while valid_idx < len(now_t) and now_t[valid_idx][0] == now_path[-1]:
            q.append((now_path + [now_t[valid_idx][1]], now_t[:valid_idx] + now_t[valid_idx+1:]))
            
            valid_idx += 1
        
    return answer