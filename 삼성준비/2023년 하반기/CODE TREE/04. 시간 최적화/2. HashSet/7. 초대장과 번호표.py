# problem link : https://www.codetree.ai/missions/8/problems/invitation-and-number-tag?&utm_source=clipboard&utm_medium=text

from collections import deque

n, g = map(int, input().split())

invited = [False] * n
groups = [set() for _ in range(g)]
people_groups = [[] for _ in range(n)]

q = deque()
ans = 0

for i in range(g):
    nums = list(map(int, input().split()))[1:]
    for num in nums:
        num -= 1
        groups[i].add(num)
        people_groups[num].append(i)

q.append(0)
invited[0] = True

while q:
    x = q.popleft()
    ans += 1

    for g_num in people_groups[x]:
        groups[g_num].remove(x)

        if len(groups[g_num]) == 1:
            p_num = list(groups[g_num])[0]
            if not invited[p_num]:
                invited[p_num] = True
                q.append(p_num)

print(ans)