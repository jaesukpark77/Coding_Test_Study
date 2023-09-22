# problem link : https://www.codetree.ai/missions/2/problems/seperate-village?&utm_source=clipboard&utm_medium=text

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

people_num = 0
people_nums = list()

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False

    if visited[x][y] or grid[x][y] == 0:
        return False

    return True

def dfs(x, y):
    global people_num
    dxs, dys, = [0, 1, 0, -1], [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        new_x, nex_y = x + dx, y + dy

        if can_go(new_x, nex_y):
            visited[new_x][nex_y] = True

            people_num += 1
            dfs(new_x, nex_y)

for i in range(n):
    for j in range(n):
        if can_go(i, j):
            visited[i][j] = True
            people_num = 1

            dfs(i, j)

            people_nums.append(people_num)

people_nums.sort()

print(len(people_nums))
for people in people_nums:
    print(people)