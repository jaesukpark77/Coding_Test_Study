# proeblem link : https://www.codetree.ai/missions/8/problems/treemap-basic?&utm_source=clipboard&utm_medium=text

from sortedcontainers import SortedDict

n = int(input())
d = SortedDict()

for _ in range(n):
    command = input()

    if command.startswith('add'):
        _, k, v = tuple(command.split())
        k, v = int(k), int(v)
        d[k] =  v
    elif command.startswith('remove'):
        k = int(command.split()[1])
        d.pop(k)
    elif command.startswith('find'):
        k = int(command.split()[1])
        if k not in d:
            print('None')
        else:
            print(d[k])
    else:
        if not d:
            print('None')
        else:
            for value in d.values():
                print(value, end=' ')
            print()
