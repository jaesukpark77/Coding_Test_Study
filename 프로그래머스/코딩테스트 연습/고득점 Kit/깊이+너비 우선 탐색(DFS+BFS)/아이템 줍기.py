# preoblem link : https://school.programmers.co.kr/learn/courses/30/lessons/87694

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    double_n = 102
    
    field = [[-1] * double_n for _ in range(double_n)]
    
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)
        
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                elif field[i][j] != 0:
                    field[i][j] = 1
                    
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    q = deque()
    q.append([characterX * 2, characterY * 2])
    visited = [[1] * double_n for _ in range(double_n)]
    
    while q:
        x, y = q.popleft()
        
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if field[nx][ny] == 1 and visited[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                
    return answer