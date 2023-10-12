# problem link : https://www.codetree.ai/training-field/frequent-problems/problems/go-on-the-rides?&utm_source=clipboard&utm_medium=text

EMPTY = 0

n = int(input())
target_num = [0] * (n * n + 1)
friends = [
    [False] * (n * n + 1)
    for _ in range(n * n + 1)
]

rides = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

def is_friend(num1, num2):
    return friends[num1][num2]

def get_curr_cell(num, x, y):
    friend_cnt, blank_cnt = 0, 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if not in_range(nx, ny):
            continue
        
        if rides[nx][ny] == EMPTY:
            blank_cnt += 1
        elif is_friend(num, rides[nx][ny]):
            friend_cnt += 1
    
    return (friend_cnt, blank_cnt, -x, -y)

def move(num):
    best_cell = (0, 0, -(n+1), -(n+1))
    for i in range(1, n+1):
        for j in range(1, n+1):
            if rides[i][j] == EMPTY:
                curr = get_curr_cell(num, i, j)

                if best_cell < curr:
                    best_cell = curr

    _, _, x, y = best_cell
    rides[-x][-y] = num

def get_score(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny) and is_friend(rides[x][y], rides[nx][ny]):
            cnt += 1
    
    return int(10 ** (cnt - 1))

def get_total_score():
    return sum([
        get_score(i, j)
        for i in range(1, n+1)
        for j in range(1, n+1)
    ])

for i in range(1, n * n + 1):
    student_data = list(map(int, input().split()))
    
    target_num[i] = student_data[0]
    for friend_num in student_data[1:]:
        friends[target_num[i]][friend_num] = True

for i in range(1, n * n + 1):
    move(target_num[i])

ans = get_total_score()

print(ans)