# problem link : https://www.codetree.ai/missions/5/problems/strange-bomb-2?utm_source=clipboard&utm_medium=text

n, k = map(int, input().split())

num = [int(input()) for _ in range(n)]

ans = -1

for i in range(n):
    for j in range(i+1, n):
        if j - i > k:
            break
        
        if num[i] != num[j]:
            continue
        
        ans = max(ans, num[i])

print(ans)