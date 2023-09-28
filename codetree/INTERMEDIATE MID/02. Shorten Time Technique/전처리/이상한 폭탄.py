# problem link : https://www.codetree.ai/missions/8/problems/strange-bomb?&utm_source=clipboard&utm_medium=text

n, k = map(int, input().split())
arr = list(int(input()) for _ in range(n))
R = [0] * n

lastest_index = dict()
for i in range(n-1, -1, -1):
    if arr[i] not in lastest_index:
        R[i] = -1
    else:
        R[i] = lastest_index[arr[i]]
    
    lastest_index[arr[i]] = i

ans = -1

for i in range(n):
    if R[i] != -1 and R[i] - i <= k:
        ans = max(ans, arr[i])

print(ans)