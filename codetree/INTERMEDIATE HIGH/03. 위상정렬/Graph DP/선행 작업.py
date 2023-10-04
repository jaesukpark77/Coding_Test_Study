# problem link : https://www.codetree.ai/missions/9/problems/predecessor?&utm_source=clipboard&utm_medium=text

from collections import deque

n = int(input())
edges = [[] for _ in range(n+1)]

indegree = [0] * (n+1)
working_time = [0] * (n+1)
dp = [0] * (n+1)

q = deque()

for i in range(1, n+1):
    working_time[i], _, *nums = tuple(map(int, input().split()))

    for x in nums:
        edges[x].append(i)
        indegree[i] += 1

for i in range(1, n+1):
    if not indegree[i]:
        q.append(i)

        dp[i] = working_time[i]

while q:
    x = q.popleft()

    for y in edges[x]:
        dp[y] = max(dp[y], dp[x] + working_time[y])

        indegree[y] -= 1

        if not indegree[y]:
            q.append(y)

ans = 0
for i in range(1, n+1):
    ans = max(ans, dp[i])

print(ans)