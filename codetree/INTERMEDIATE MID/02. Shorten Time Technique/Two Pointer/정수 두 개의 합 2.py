# problem link : https://www.codetree.ai/missions/8/problems/sum-of-two-integers-2?&utm_source=clipboard&utm_medium=text

n, k = map(int, input().split())
arr = [0] + [int(input()) for _ in range(n)]

arr.sort()

ans = 0
j = n

for i in range(1, n+1):
    while j != 1 and arr[i] + arr[j] > k:
        j -= 1
    
    if j <= i:
        break

    ans += j - i

print(ans)