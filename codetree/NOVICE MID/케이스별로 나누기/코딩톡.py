# problem link : https://www.codetree.ai/missions/5/problems/coding-talk?&utm_source=clipboard&utm_medium=text

import sys

n, m, p = map(int, input().split())

message = [list(input().split()) for _ in range(m)]

if int(message[p-1][1]) == 0:
    sys.exit()

for i in range(n):
    person = chr(ord('A') + i)
    read = False

    for c, u in message:
        u = int(u)
        if u >= int(message[p-1][1]) and c == person:
            read = True

    if read == False:
        print(person, end=' ')