# problem link : https://www.codetree.ai/missions/8/problems/problem-recommendation-system-1?&utm_source=clipboard&utm_medium=text

from sortedcontainers import SortedSet

n = int(input())
problems = SortedSet()

for _ in range(n):
    p, l = tuple(map(int, input().split()))

    problems.add((l, p))

m = int(input())

for _ in range(m):
    command = input()

    if command.startswith('ad'):
        _, p, l = command.split()
        p, l = int(p), int(l)

        problems.add((l, p))
    elif command.startswith('sv'):
        _, p, l = command.split()
        p, l = int(p), int(l)

        problems.remove((l, p))
    else:
        x = int(command.split()[1])

        if x == 1:
            _, p = problems[-1]
            print(p)
        else:
            _, p = problems[0]
            print(p)