# problem link : https://www.codetree.ai/missions/8/problems/make-biggest-num?&utm_source=clipboard&utm_medium=text

from functools import cmp_to_key

n = int(input())
arr = [int(input()) for _ in range(n)]

def compare(a, b):
    if str(a) + str(b) > str(b) + str(a):
        return -1
    if str(a) + str(b) < str(b) + str(a):
        return 1
    else:
        return 0

arr.sort(key = cmp_to_key(compare))

for elem in arr:
    print(elem, end='')