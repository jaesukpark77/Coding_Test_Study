# problem link : https://www.codetree.ai/missions/2/problems/backward-permutation?&utm_source=clipboard&utm_medium=text

n = int(input())
visited = [False] * (n + 1)
picked = []

def get_permutation(cnt):
    if cnt == n:
        for elem in picked:
            print(elem, end=' ')
        print()

    for i in range(n, 0, -1):
        if visited[i]:
            continue

        visited[i] = True
        picked.append(i)

        get_permutation(cnt + 1)

        visited[i] = False
        picked.pop()

get_permutation(0)