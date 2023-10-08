# problem link : https://www.codetree.ai/missions/2/problems/seperate-village?&utm_source=clipboard&utm_medium=text

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

people_num = 0
people_nums = []

# 주어진 위치가 격자를 벗어나는지 여부를 반환
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 주어진 위치로 이동할 수 있는지 여부를 확인
def can_go(x, y):
    if not in_range(x, y):
        return False
    
    if visited[x][y] or grid[x][y] == 0:
        return False

    return True

def dfs(x, y):
    global people_num

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny):
            visited[nx][ny] = True

            people_num += 1
            dfs(nx, ny)

# 격자의 각 위치에서 탐색을 시작할 수 있는 경우 한 마을에 대한 DFS 탐색을 수행
for i in range(n):
    for j in range(n):
        if can_go(i, j):
            # 해당 위치를 방문할 수 있는 경우 visited 배열을 갱신하고 새로운 마을을 탐색한다는 의미로 people_num을 1으로 갱신
            visited[i][j] = True
            people_num = 1

            dfs(i, j)
            # 한 마을에 대한 탐색이 끝난 경우 마을 내의 사람 수를 저장
            people_nums.append(people_num)

people_nums.sort()
print(len(people_nums))
for elem in people_nums:
    print(elem)