# problem link : https://www.codetree.ai/missions/2/problems/select-segments-without-overlap-2?&utm_source=clipboard&utm_medium=text

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
dp = [0] * n

segments.sort()

for i in range(n):
    dp[i] = 1

    for j in range(i):
        x1_i, _ = segments[i]
        _, x2_j = segments[j]

        if x2_j < x1_i:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))