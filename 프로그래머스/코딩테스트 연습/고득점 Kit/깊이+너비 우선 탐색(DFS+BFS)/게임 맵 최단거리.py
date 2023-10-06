# problem link : https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    q = deque()
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited[0][0] = True
    q.append((0, 0))
    
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx and nx < n and 0 <= ny and ny < m and maps[nx][ny] == 1:
                if not visited[nx][ny]:
                    visited[x][ny] = True
                    q.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1
                    
    if maps[n - 1][m - 1] == 1:
        return -1
    else:
        return maps[n - 1][m - 1]

# code 리팩토링 과정 - 함수화

from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    def in_range(x, y):
        return 0 <= x and x < n and 0 <= y and y < m
    
    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[x][y] = True
        
        while q:
            x, y = q.popleft()
            
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                
                if in_range(nx, ny) and maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))
        
        return maps[n - 1][m - 1]
                
    answer = bfs(0, 0)
            
    return -1 if answer == 1 else answer