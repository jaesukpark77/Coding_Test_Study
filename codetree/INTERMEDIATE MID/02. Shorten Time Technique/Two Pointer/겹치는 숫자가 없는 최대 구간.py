# problem link : https://www.codetree.ai/missions/8/problems/max-interval-without-overlapping-numbers?&utm_source=clipboard&utm_medium=text

MAX_R = 100000

n = int(input())
arr = [0] + list(map(int, input().split()))
count_arr = [0] * (MAX_R + 1)

ans = 0

j = 0

for i in range(1, n+1):
    while j + 1 <= n and count_arr[arr[j+1]] != 1:
        count_arr[arr[j+1]] += 1
        j += 1

    ans = max(ans, j - i + 1)

    count_arr[arr[i]] -= 1

print(ans)