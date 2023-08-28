# problem link : https://www.codetree.ai/missions/5/problems/strange-bomb-3?&utm_source=clipboard&utm_medium=text

MAX_A = 1000000
n, k = map(int, input().split())

num = [int(input()) for _ in range(n)]

bomb = [0] * (MAX_A + 1)
explode = [False] * n

maxval = 1
maxidx = 0

for i in range(n):
    for j in range(i + 1, n):
        if j - i > k:
            break

        if num[i] != num[j]:
            continue

        if explode[i] == False:
            bomb[num[i]] += 1;
            explode[i] = True

        if explode[j] == False:
            bomb[num[j]] += 1;
            explode[j] = True

for i in range(MAX_A + 1):
    if maxval <= bomb[i]:
        maxval = bomb[i]
        maxidx = i

print(maxidx)