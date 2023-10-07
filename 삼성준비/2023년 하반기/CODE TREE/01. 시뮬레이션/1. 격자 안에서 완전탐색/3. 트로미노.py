# problem link : https://www.codetree.ai/missions/2/problems/tromino?&utm_source=clipboard&utm_medium=text

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

shapes = [
    [[1, 1, 0],
    [1, 0, 0],
    [0, 0, 0]],

    [[1, 1, 0],
    [0, 1, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[0, 1, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[1, 1, 1],
    [0, 0, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]],
]

def get_max_sum(x, y):
    max_sum = 0
    for i in range(6):
        is_possible = True
        sum_of_nums = 0

        for dx in range(3):
            for dy in range(3):
                if shapes[i][dx][dy] == 0:
                    continue
                elif x + dx >= n or y + dy >= m: # n x m 배열의 경우 범위 잘 신경쓰기!!!
                    is_possible = False
                else:
                    sum_of_nums += grid[x + dx][y + dy]

        if is_possible:
            max_sum = max(max_sum, sum_of_nums)

    return max_sum

ans = 0

for i in range(n):
    for j in range(m):
        ans = max(ans, get_max_sum(i, j))

print(ans)