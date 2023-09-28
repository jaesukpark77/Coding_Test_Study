# problem link : https://www.codetree.ai/missions/8/problems/rock-paper-scissors-to-see-the-future?&utm_source=clipboard&utm_medium=text

n = int(input())
matches = [input() for _ in range(n)]

L, R = [0] * n, [0] * n
ans = 0

for shape in 'PHS':
    same_cnt = 0

    for i in range(n):
        if matches[i] == shape:
            same_cnt += 1
        
        L[i] = max(L[i], same_cnt)

for shape in 'PHS':
    same_cnt = 0
    for i in range(n-1, -1, -1):
        if matches[i] == shape:
            same_cnt += 1

        R[i] = max(R[i], same_cnt)

for i in range(n-1):
    ans = max(ans, L[i] + R[i+1])

print(ans)