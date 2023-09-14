# problem link : https://www.codetree.ai/missions/5/problems/finding-a-b-c?&utm_source=clipboard&utm_medium=text

n = 7
arr = list(map(int, input().split()))

arr.sort()
a, b = arr[0], arr[1]
c = arr[-1] - a - b

print(a, b, c)