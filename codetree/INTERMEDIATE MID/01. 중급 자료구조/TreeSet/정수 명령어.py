# problem link : https://www.codetree.ai/missions/8/problems/Integer-command?&utm_source=clipboard&utm_medium=text

from sortedcontainers import SortedSet

t = int(input())
for _ in range(t):
    n = int(input())
    s = SortedSet()

    for _ in range(n):
        command, x = tuple(input().split())
        x = int(x)

        if command == 'I':
            s.add(x)
        elif command == 'D' and s:
            if x == 1:
                s.remove(s[-1])
            else:
                s.remove(s[0])

    if not s:
        print('EMPTY')
    else:
        print(s[-1], s[0])