# problem link : https://www.codetree.ai/missions/2/problems/number-of-happy-sequence?&utm_source=clipboard&utm_medium=text

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

seq = [0] * n

def is_happy_sequence():
    consecutive_count, max_cnt = 1, 1
    for i in range(1, n):
        if seq[i - 1] == seq[i]:
            consecutive_count += 1
        else:
            consecutive_count = 1

        max_cnt = max(max_cnt, consecutive_count)
    
    return max_cnt >= m

ans = 0

for i in range(n):
    seq = grid[i][:]

    if is_happy_sequence():
        ans += 1

for j in range(n):
    for i in range(n):
        seq[i] = grid[i][j]

    if is_happy_sequence():
        ans += 1

print(ans)