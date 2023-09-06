# problem link : https://www.codetree.ai/missions/6/problems/sequence-manipulation?&utm_source=clipboard&utm_medium=text

from collections import deque

n = int(input())
dq = deque()

for i in range(1, n+1):
    dq.append(i)

while len(dq) > 1:
    dq.popleft()
    dq.append(dq[0])
    dq.popleft()

print(dq[0])