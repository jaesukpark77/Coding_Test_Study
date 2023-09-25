# problem link : https://www.codetree.ai/missions/8/problems/hashset-basic?&utm_source=clipboard&utm_medium=text

n = int(input())
s = set()

for _ in range(n):
    command, x = tuple(input().split())

    if command == 'add':
        s.add(x)
    elif command == 'remove':
        s.remove(x)
    else:
        if x in s:
            print('true')
        else:
            print('false')