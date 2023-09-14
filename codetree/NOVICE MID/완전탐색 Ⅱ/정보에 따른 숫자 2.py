# problem link : https://www.codetree.ai/missions/5/problems/number-based-on-information-2?utm_source=clipboard&utm_medium=text

import sys

INT_MAX = sys.maxsize

t, a, b = map(int, input().split())

sn_data = [tuple(input().split()) for _ in range(t)]

ans = 0
for i in range(a, b+1):
    distance_s = INT_MAX
    distance_n = INT_MAX

    for p, q in sn_data:
        q = int(q)

        if p == 'S':
            distance_s = min(distance_s, abs(q - i))
        else:
            distance_n = min(distance_n, abs(q - i))

    if distance_s <= distance_n:
        ans += 1

print(ans)