# problem link : https://www.codetree.ai/missions/2/problems/marble-movement?&utm_source=clipboard&utm_medium=text

n, m, t, k = map(int, input().split())
grid = [[[] for _ in range(n)]for _ in range(n)]
next_grid = [[[] for _ in range(n)]for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def next_pos(x, y, vnum, move_dir):
    dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]
    
    for _ in range(vnum):
        nx, ny = x + dxs[move_dir], y + dys[move_dir]

        if not in_range(nx, ny):
            move_dir = 3 - move_dir
            nx, ny = x + dxs[move_dir], y + dys[move_dir]
        x, y = nx, ny

    return (x, y, move_dir)

def move_all():
    for x in range(n):
        for y in range(n):
            for v, num, move_dir in grid[x][y]:
                next_x, next_y, next_dir = next_pos(x, y, v, move_dir)
                next_grid[next_x][next_y].append((v, num, next_dir))

def select_marbles():
    for i in range(n):
        for j in range(n):
            if len(next_grid[i][j]) >= k:
                next_grid[i][j].sort(lambda x: (-x[0], -x[1]))
                while len(next_grid[i][j]) > k:
                    next_grid[i][j].pop()

def simulate():
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = []
		
    move_all()
    
    select_marbles()
    
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]


dir_mapper = {
    "U": 0,
    "R": 1,
    "L": 2,
    "D": 3
}

for i in range(m):
    r, c, d, v = input().split()
    r, c, v = map(int, [r, c, v])

    grid[r - 1][c - 1].append((v, i + 1, dir_mapper[d]))

for _ in range(t):
    simulate()

ans = sum([
    len(grid[i][j])
    for i in range(n)
    for j in range(n)
])

print(ans)