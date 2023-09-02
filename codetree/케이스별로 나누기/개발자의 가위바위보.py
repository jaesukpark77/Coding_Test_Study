# problem link : https://www.codetree.ai/missions/5/problems/developer's-rock-paper-scissors?&utm_source=clipboard&utm_medium=text

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_win = 0

win = 0
for a, b in arr:
    if a == 1 and b == 2:
        win += 1
    elif a == 2 and b == 3:
        win += 1
    elif a == 3 and b == 1:
        win += 1

max_win = max(max_win, win)

win = 0
for a, b in arr:
    if a == 1 and b == 3:
        win += 1
    elif a == 3 and b == 2:
        win += 1
    elif a == 2 and b == 1:
        win += 1

max_win = max(max_win, win)

print(max_win)