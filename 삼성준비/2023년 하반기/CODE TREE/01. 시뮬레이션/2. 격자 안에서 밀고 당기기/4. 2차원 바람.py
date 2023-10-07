# problem link : https://www.codetree.ai/missions/2/problems/The-2D-wind-blows?&utm_source=clipboard&utm_medium=text

n, m, q = map(int, input().split())
a = [[0 for _ in range(m+1)] for _ in range(n+1)]
temp_arr = [[0 for _ in range(m+1)] for _ in range(n+1)]

def rotate(start_row, start_col, end_row, end_col):
    temp = a[start_row][start_col]

    for row in range(start_row, end_row):
        a[row][start_col] = a[row+1][start_col]

    for col in range(start_col, end_col):
        a[end_row][col] = a[end_row][col + 1]

    for row in range(end_row, start_row, -1):
        a[row][end_col] = a[row - 1][end_col]

    for col in range(end_col, start_col, -1):
        a[start_row][col] = a[start_row][col - 1]

    a[start_row][start_col + 1] = temp


def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= m

def average(x, y):
    dxs, dys = [0, 1, -1, 0, 0], [0, 0, 0, 1, -1]

    active_numbers = [
        a[x + dx][y + dy]
        for dx, dy in zip(dxs, dys)
        if in_range(x + dx, y + dy)
    ]

    return sum(active_numbers) // len(active_numbers)

def set_average(start_row, start_col, end_row, end_col):
    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            temp_arr[row][col] = average(row, col)
    
    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            a[row][col] = temp_arr[row][col]

def simulate(start_row, start_col, end_row, end_col):
    rotate(start_row, start_col, end_row, end_col)
    set_average(start_row, start_col, end_row, end_col)

for row in range(1, n+1):
    given_nums = list(map(int, input().split()))
    for col, num in enumerate(given_nums, start = 1):
        a[row][col] = num

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    simulate(r1, c1, r2, c2)

for row in range(1, n+1):
    for col in range(1, m+1):
        print(a[row][col], end= ' ')
    print()