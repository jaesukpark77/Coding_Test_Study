# problem link : https://www.codetree.ai/missions/8/problems/flip-up-down-left-right?&utm_source=clipboard&utm_medium=text

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dxs, dys = [0, 0, 1, 0, -1], [0, 1, 0, -1, 0]

cnt = 0
for i in range(1, n):
    for j in range(0, n):
        if arr[i-1][j] == 0:
            cnt += 1
            for dx, dy in zip(dxs, dys):
                x = i + dx
                y = j + dy
                
                if in_range(x, y):
                    arr[x][y] = 1 - arr[x][y]

possible = True

for elem in arr[n-1]:
    if elem != 1:
        possible = False

if possible == False:
    print(-1)
else:
    print(cnt)