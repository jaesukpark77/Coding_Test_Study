# problem link : https://school.programmers.co.kr/learn/courses/30/lessons/43162

# DFS Method

def DFS(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1:
            if visited[connect] == False:
                DFS(n, computers, connect, visited)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            answer += 1
    return answer

# BFS Method - stack 활용

def BFS(n, computers, com, visited):
    visited[com] = True
    queue = []
    queue.append(com)
    
    while len(queue) != 0:
        com = queue.pop(0)
        visited[com] = True
        
        for connect in range(n):
            if connect != com and computers[com][connect] == 1:
                if not visited[connect]:
                    queue.append(connect)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for com in range(n):
        if not visited[com]:
            BFS(n, computers, com, visited)
            answer += 1
    return answer

# BFS Method - deque 활용

from collections import deque

def BFS(n, computers, com, visited):
    visited[com] = True
    queue = deque()
    queue.append(com)
    
    while len(queue) != 0:
        com = queue.popleft()
        visited[com] = True
        
        for connect in range(n):
            if connect != com and computers[com][connect] == 1:
                if not visited[connect]:
                    queue.append(connect)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for com in range(n):
        if not visited[com]:
            BFS(n, computers, com, visited)
            answer += 1
    return answer


