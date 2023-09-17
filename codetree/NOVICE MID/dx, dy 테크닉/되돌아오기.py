# problem link : https://www.codetree.ai/missions/5/problems/come-back?&utm_source=clipboard&utm_medium=text

n = int(input())

x, y = 0, 0
dxs, dys = [1, -1, 0, 0], [0, 0, -1, 1]
ans = -1

elasped_time = 0

def move(move_dir, dist):
    global x, y
    global ans, elasped_time

    for _ in range(dist):
        x, y = x + dxs[move_dir], y + dys[move_dir]

        elasped_time += 1

        if x == 0 and y == 0:
            ans = elasped_time
            return True

    return False

for _ in range(n):
    curr_dir, dist = input().split()
    dist = int(dist)

    if curr_dir == 'E':
        move_dir = 0
    elif curr_dir == 'W':
        move_dir = 1
    elif curr_dir == 'S':
        move_dir = 2
    else:
        move_dir = 3
    
    done = move(move_dir, dist)

    if done:
        break

print(ans)