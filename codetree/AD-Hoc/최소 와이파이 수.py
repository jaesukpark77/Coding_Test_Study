# problem link : https://www.codetree.ai/missions/5/problems/minimum-number-of-wifi?&utm_source=clipboard&utm_medium=text

n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt, i = 0, 0

while i < n:
    if arr[i] == 1:
        cnt += 1
        i += 2 * m + 1
    else:
        i += 1

print(cnt)