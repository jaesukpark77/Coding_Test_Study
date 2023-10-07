# problem link : https://www.codetree.ai/missions/2/problems/gold-mining/description

n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def get_area(k):
    return k * k + (k + 1) * (k + 1)

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def get_num_of_gold_in_border(row, col, k):
    dxs, dys = [1, 1, -1, -1], [-1, 1, 1, -1]
    
    if k == 0:
        return grid[row][col]
    
    num_of_gold = 0
    
    curr_x, curr_y = row - k, col # 순회 시작점 설정
    for dx, dy in zip(dxs, dys):
        for step in range(k):
            if in_range(curr_x, curr_y):
                num_of_gold += grid[curr_x][curr_y]

            curr_x = curr_x + dx
            curr_y = curr_y + dy
    
    return num_of_gold

max_gold = 0

for row in range(n):
    for col in range(n):
        num_of_gold = 0
        for k in range(2 * (n - 1) + 1):
            num_of_gold += get_num_of_gold_in_border(row, col, k)
            
            if num_of_gold * m >= get_area(k):
                max_gold = max(max_gold, num_of_gold)

print(max_gold)