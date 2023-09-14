# problem link : https://www.codetree.ai/missions/5/problems/ya-rock?&utm_source=clipboard&utm_medium=text

MAX_NUM = 3

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

max_score = 0

for i in range(1, MAX_NUM+1):
    yabawi = [0] * 4
    yabawi[i] = 1

    score = 0
    for a, b, c in arr:
        yabawi[a], yabawi[b] = yabawi[b], yabawi[a]

        if yabawi[c] == 1:
            score += 1
    
    max_score = max(max_score, score)

print(max_score)