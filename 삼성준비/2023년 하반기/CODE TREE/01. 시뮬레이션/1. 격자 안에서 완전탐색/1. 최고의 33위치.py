# problem link : https://www.codetree.ai/missions/2/problems/best-place-of-33/explanation

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# (row_s, col_s) ~ (row_e, col_e) 사이의 금의 갯수 계산
def get_num_of_gold(row_s, col_s, row_e, col_e):
    num_of_gold = 0

    for row in range(row_s, row_e + 1):
        for col in range(col_s, col_e + 1):
            num_of_gold += grid[row][col]

    return num_of_gold

max_gold = 0

for row in range(n):
    for col in range(n):
        # row와 col이 0부터 시작이므로 >=n
        # 만약 row와 col이 1부터 시작이면 > n
        if row + 2 >= n or col + 2 >= n:
            continue
        
        num_of_gold = get_num_of_gold(row, col, row + 2, col + 2)

        max_gold = max(max_gold, num_of_gold)

print(max_gold)