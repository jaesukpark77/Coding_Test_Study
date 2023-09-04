# problem link : https://www.codetree.ai/missions/5/problems/reorder-sequence?&utm_source=clipboard&utm_medium=text

n = int(input())
blocks = list(map(int, input().split()))

idx = n - 2
while idx >= 0 and blocks[idx] < blocks[idx + 1]:
    idx -= 1

print(idx + 1)