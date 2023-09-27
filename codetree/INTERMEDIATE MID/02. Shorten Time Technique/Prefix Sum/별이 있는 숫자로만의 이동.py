# problem link : https://www.codetree.ai/missions/8/problems/move-to-numbers-with-star?&utm_source=clipboard&utm_medium=text

n, k = map(int, input().split())
arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
s = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(n):
    board = list(map(int, input().split()))
    for j in range(n):
        arr[i+1][j+1] = board[j]

ans = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        s[i][j] = s[i][j - 1] + arr[i][j]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        sum_all = 0
        for r in range(i - k, i + k + 1):
            c = k - abs(i - r)

            if 1 <= r and r <= n:
                sum_all += s[r][min(j + c, n)] - s[r][max(j - c - 1, 0)]
        
        ans = max(ans, sum_all)

print(ans)