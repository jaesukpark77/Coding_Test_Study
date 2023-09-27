# problem link : https://www.codetree.ai/missions/8/problems/the-number-of-characters-in-the-interval?&utm_source=clipboard&utm_medium=text

MAX_C = 3

n, m, k = tuple(map(int, input().split()))
arr = [[0] * (m + 1) for _ in range(n + 1)]
prefix_sum = [[[0] * (m + 1) for _ in range(n + 1)] for _ in range(MAX_C + 1)]

def get_sum(c, x1, y1, x2, y2):
    return prefix_sum[c][x2][y2] - prefix_sum[c][x1-1][y2] - prefix_sum[c][x2][y1-1] + prefix_sum[c][x1-1][y1-1]

for i in range(1, n+1):
    row = input()
    for j in range(1, m+1):
        if row[j-1] == 'a':
            arr[i][j] = 1
        elif row[j - 1] == 'b':
            arr[i][j] = 2
        else:
            arr[i][j] = 3

for c in range(1, 4):
    for i in range(1, n+1):
        for j in range(1, m+1):
            additional_value = 0

            if arr[i][j] == c:
                additional_value = 1

            prefix_sum[c][i][j] = prefix_sum[c][i - 1][j] + \
                            prefix_sum[c][i][j - 1] - \
                            prefix_sum[c][i - 1][j - 1] + \
                            additional_value

for _ in range(k):
    x1, y1, x2, y2 = tuple(map(int, input().split()))

    print(get_sum(1, x1, y1, x2, y2),
          get_sum(2, x1, y1, x2, y2),
          get_sum(3, x1, y1, x2, y2))