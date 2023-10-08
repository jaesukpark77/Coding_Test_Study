# problem link : https://www.codetree.ai/missions/2/problems/big-explosion?&utm_source=clipboard&utm_medium=text
 
n, m, r, c = map(int, input().split())
grid = [[0] * n for _ in range(n)]
next_grid = [[0] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def expand(x, y, dist):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx * dist , y + dy * dist
        
        if in_range(nx, ny):
            next_grid[nx][ny] = 1

def simulate(dist):
    # Step1. next_grid 값을 0으로 초기화합니다.
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0

    # Step2. 폭탄을 던지는 시뮬레이션을 진행합니다.
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                expand(i, j, dist)
    
    # Step3. next_grid 값을 grid로 업데이트 해줍니다.
    for i in range(n):
        for j in range(n):
            if next_grid[i][j]:
                grid[i][j] = 1

grid[r-1][c-1] = 1

dist = 1
for _ in range(m):
    simulate(dist)
    dist *= 2

ans = sum([
    grid[i][j] for i in range(n) for j in range(n)
])

print(ans)