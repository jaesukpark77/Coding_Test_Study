# problem link : https://www.codetree.ai/training-field/frequent-problems/problems/tree-kill-all?&utm_source=clipboard&utm_medium=text

n, m, k, c = map(int, input().split())
tree = [[0] * (n + 1)]

for _ in range(n):
    tree.append([0] + list(map(int, input().split())))

add_tree = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

herb = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

ans = 0

def is_out_range(x, y):
    return not (1 <= x and x <= n and 1 <= y and y <= n)

def step_one():
    dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if tree[i][j] <= 0:
                continue

            cnt = 0
            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy

                if is_out_range(nx, ny):
                    continue
                
                if tree[nx][ny] > 0:
                    cnt += 1

            tree[i][j] += cnt

def step_two():
    dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            add_tree[i][j] = 0

    for i in range(1, n+1):
        for j in range(1, n+1):
            if tree[i][j] <= 0:
                continue

            cnt = 0

            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy
                if is_out_range(nx, ny):
                    continue
                if herb[nx][ny]:
                    continue
                if tree[nx][ny] == 0:
                    cnt += 1

            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy
                if is_out_range(nx, ny):
                    continue
                if herb[nx][ny]:
                    continue
                if tree[nx][ny] == 0:
                    add_tree[nx][ny] += tree[i][j] // cnt

    for i in range(1, n+1):
        for j in range(1, n+1):
            tree[i][j] += add_tree[i][j]

def step_three():
    global ans

    dxs, dys = [-1, 1, 1, -1], [-1, -1, 1, 1]

    max_del, max_x, max_y = 0, 1, 1

    for i in range(1, n+1):
        for j in range(1, n+1):
            if tree[i][j] <= 0:
                continue
            
            cnt = tree[i][j]

            for dx, dy in zip(dxs, dys):
                nx, ny = i, j

                for _ in range(k):
                    nx, ny = nx + dx, ny + dy
                    if is_out_range(nx, ny):
                        break
                    if tree[nx][ny] <= 0:
                        break
                    cnt += tree[nx][ny]

            if max_del < cnt:
                max_del = cnt
                max_x = i
                max_y = j

    ans += max_del

    if tree[max_x][max_y] > 0:
        tree[max_x][max_y] = 0
        herb[max_x][max_y] = c

        for dx, dy in zip(dxs, dys):
            nx, ny = max_x, max_y
            for _ in range(k):
                nx, ny = nx + dx, ny + dy
                if is_out_range(nx, ny): 
                    break
                if tree[nx][ny] < 0: 
                    break
                if tree[nx][ny] == 0:
                    herb[nx][ny] = c
                    break

                tree[nx][ny] = 0
                herb[nx][ny] = c

def delete_herb():
    for i in range(1, n + 1):
        for j in range(1, n + 1): 
            if herb[i][j] > 0: 
                herb[i][j] -= 1

for _ in range(m):
    step_one()
    step_two()
    delete_herb()
    step_three()

print(ans)