# problem link : https://www.codetree.ai/missions/8/problems/first-appearing-position?&utm_source=clipboard&utm_medium=text

from sortedcontainers import SortedDict

n = int(input())
arr = list(map(int, input().split()))

first_appear = SortedDict()

for i in range(n):
    if arr[i] not in first_appear:
        first_appear[arr[i]] = i + 1

for num, cnt in first_appear.items():
    print(num, cnt)