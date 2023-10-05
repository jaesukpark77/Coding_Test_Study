# problem link : https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    v = [False] * (len(words))
    
    while q:
        word, cnt = q.popleft()
        
        if word == target:
            answer = cnt
            break
        
        for i in range(len(words)):
            tmp_cnt = 0
            
            if not v[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        tmp_cnt += 1
                        
            if tmp_cnt == 1:
                q.append([words[i], cnt + 1])
                v[i] = True

    return answer