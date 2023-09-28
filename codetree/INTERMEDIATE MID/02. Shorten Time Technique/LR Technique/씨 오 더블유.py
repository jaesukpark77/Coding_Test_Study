# problem link : https://www.codetree.ai/missions/8/problems/c-o-w?&utm_source=clipboard&utm_medium=text

n = int(input())
word = input()
L, R = [0] * n, [0] * n
ans = 0

L[0] = 1 if word[0] == 'C' else 0

for i in range(1, n):
    L[i] = L[i - 1] + (1 if word[i] == 'C' else 0)

R[n-1] = 1 if word[n-1] == 'W' else 0
for i in range(n-2, -1, -1):
    R[i] = R[i+1] + (1 if word[i] == 'W' else 0)

for i in range(1, n-1):
    if word[i] == 'O':
        ans += L[i - 1] * R[i + 1]

print(ans)