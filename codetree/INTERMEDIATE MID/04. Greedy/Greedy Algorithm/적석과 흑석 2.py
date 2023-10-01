# problem link : https://www.codetree.ai/missions/8/problems/red-stone-and-black-stone-2?&utm_source=clipboard&utm_medium=text

from sortedcontainers import SortedSet

c, n = map(int, input().split())
red_stones = [int(input()) for _ in range(c)]
black_stones = []
for _ in range(n):
    a, b = tuple(map(int, input().split()))
    black_stones.append((b, a))

red_s = SortedSet(red_stones)
black_stones.sort()

ans = 0
for b, a in black_stones:
    idx = red_s.bisect_left(a)

    if idx != len(red_s):
        ti = red_s[idx]

        if ti <= b:
            ans += 1
            red_s.remove(ti)

print(ans)