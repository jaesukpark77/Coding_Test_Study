# problem link : https://www.codetree.ai/missions/5/problems/location-of-the-second-smallest-number?&utm_source=clipboard&utm_medium=text

import sys

n = int(input())
a = list(map(int, input().split()))

myarr = sorted(a)

isexist = False
low2 = 0
for elem in myarr:
    if elem != myarr[0]:
        low2 = elem
        isexist = True
        break

if isexist == False:
    print(-1)
    sys.exit()

ansidx = -1
for idx, elem in enumerate(a):
    if elem == low2:
        if ansidx != -1:
            print(-1)
            sys.exit()

        ansidx = idx

print(ansidx + 1)