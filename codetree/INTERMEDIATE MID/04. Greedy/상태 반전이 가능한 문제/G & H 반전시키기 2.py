# problem link : https://www.codetree.ai/missions/8/problems/reversing-g-and-h-2?&utm_source=clipboard&utm_medium=text

n = int(input())
a = input()
b = input()

cnt = 0
for i in range(n-1, -1, -1):
    if a[i] != b[i] and cnt % 2 == 0:
        cnt += 1

    elif a[i] == b[i] and cnt % 2 == 1:
        cnt += 1

print(cnt)