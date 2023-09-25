# problem link : https://www.codetree.ai/missions/8/problems/distinct-numbers?&utm_source=clipboard&utm_medium=text

n = int(input())
arr = list(map(int, input().split()))

s = set(arr)
print(len(s))