# problem link : https://www.codetree.ai/missions/2/problems/snake-loves-apples?&utm_source=clipboard&utm_medium=text

n, m, k = map(int, input().split())
apple = [[False for _ in range(n+1)] for _ in range(n+1)]

snake = [(1, 1)]

mapper = {
    'D' : 0,
    'U' : 1,
    'R' : 2,
    'L' : 3
}

ans = 0

def can_go(x, y):
    return 1 <= x and x <= n and 1 <= y and  y <= n

def is_twisted(new_head):
    return new_head in snake

def push_front(new_head):
    if is_twisted(new_head):
        return False
    
    snake.insert(0, new_head)

    return True

def pop_back():
    snake.pop()

def move_snake(nx, ny):
    if apple[nx][ny]:
        apple[nx][ny] = False

        if not push_front((nx, ny)):
            return False
        else:
            pop_back()

            if not push_front((nx, ny)):
                return False

    return True

def move(move_dir, num):
    global ans

    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

    for _ in range(num):
        ans += 1

        (head_x, head_y) = snake[0]
        nx = head_x + dxs[move_dir]
        ny = head_y + dys[move_dir]

        if not can_go(nx, ny):
            return False
        
        if not move_snake(nx, ny):
            return False
    
    return True

for _ in range(m):
    x, y = map(int, input().split())
    apple[x][y] = True

for _ in range(k):
    move_dir, num = input().split()
    num = int(num)

    if not move(mapper[move_dir], num):
        break

print(ans)