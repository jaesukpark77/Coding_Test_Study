# problem link : https://www.codetree.ai/missions/8/problems/treeset-basic?&utm_source=clipboard&utm_medium=text

from sortedcontainers import SortedSet

n = int(input())
s = SortedSet()

for _ in range(n):
    command = input()

    if command.startswith('add'):
        x = int(command.split()[1])
        s.add(x)
    elif command.startswith('remove'):
        x = int(command.split()[1])
        s.remove(x)
    elif command.startswith('find'):
        x = int(command.split()[1])
        print('true' if x in s else 'false')
    elif command.startswith("lower_bound"):
        x = int(command.split()[1])
        idx = s.bisect_left(x)

        if idx < len(s):
            print(s[idx])
        else:
            print('None')
    elif command.startswith('upper_bound'):
        x = int(command.split()[1])
        idx = s.bisect_right(x)

        if idx < len(s):
            print(s[idx])
        else:
            print('None')
    elif command == 'largest':
        if s:
            print(s[-1])
        else:
            print('None')
    else:
        if s:
            print(s[0])
        else:
            print('None')