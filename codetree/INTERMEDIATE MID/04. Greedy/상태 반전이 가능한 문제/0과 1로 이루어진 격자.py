# problem link : https://www.codetree.ai/missions/8/problems/grid-consisting-of-0-and-1?&utm_source=clipboard&utm_medium=text

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

cnt = 0

for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if arr[i][j] == 1:
            cnt += 1

            for k in range(0, i + 1):
                for l in range(0, j + 1):
                    arr[k][l] = 1 - arr[k][l]

print(cnt)