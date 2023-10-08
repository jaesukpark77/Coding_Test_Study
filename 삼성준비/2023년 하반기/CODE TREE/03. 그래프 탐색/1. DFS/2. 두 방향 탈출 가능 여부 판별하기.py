# problem link : https://www.codetree.ai/missions/2/problems/determine-escapableness-with-2-ways?&utm_source=clipboard&utm_medium=text

# SOLUTION 1

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False

    if visited[x][y] or grid[x][y] == 0:
        return False
    
    return True

def dfs(x, y):
    dxs, dys = [0, 1], [1, 0]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y):
            visited[new_x][new_y] = 1
            dfs(new_x, new_y)

visited[0][0] = 1
dfs(0, 0)

print(visited[n-1][m-1])

# SOLUTION 2

n, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _ in range(m)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    
    if visited[x][y] or grid[x][y] == 0:
        return False
    
    return True


def dfs(x, y):
    dxs, dys = [0, 1], [1, 0]
    
    # 탐색을 시작하기 전에 해당 위치를 방문했음을 표시해줍니다.
    visited[x][y] = 1
    
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        
        if can_go(new_x, new_y):
            dfs(new_x, new_y)
            
            
dfs(0, 0)

print(visited[n - 1][m - 1])