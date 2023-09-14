# problem link : https://www.codetree.ai/missions/5/problems/find-a-b-c-d?&utm_source=clipboard&utm_medium=text

n = 15

arr = list(map(int, input().split()))
arr.sort()

a, b, c = arr[0], arr[1], arr[2]

d = arr[-1] - a - b - c

print(a, b, c, d)