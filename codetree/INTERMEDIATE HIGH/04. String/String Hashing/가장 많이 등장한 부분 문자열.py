# problem link : https://www.codetree.ai/missions/9/problems/most-common-substring?&utm_source=clipboard&utm_medium=text

l, text = tuple(input().split())
l = int(l)

n = len(text)

p = [31, 37]
m = [int(1e9) + 7, int(1e9) + 9]

p_pow = [[0] * (n + 1) for _ in range(2)]

freq = {}

ans = 0

def to_int(c):
    return ord(c) - ord('a') + 1

for k in range(2):
    # p_pow[i] = p^i % m
    p_pow[k][0] = 1
    for i in range(1, n + 1):
        p_pow[k][i] = (p_pow[k][i - 1] * p[k]) % m[k]

t_h = [0, 0]
for k in range(2):
    for i in range(l):
        t_h[k] = (t_h[k] + to_int(text[i]) * p_pow[k][l - 1 - i]) % m[k]

freq[(t_h[0], t_h[1])] = freq.get((t_h[0], t_h[1]), 0) + 1
ans = max(ans, freq[(t_h[0], t_h[1])])

ans = -1
for i in range(1, n - l + 1):
    for k in range(2):
        t_h[k] = (t_h[k] * p[k] - to_int(text[i - 1]) * p_pow[k][l] + to_int(text[i + l - 1])) % m[k]

        if t_h[k] < 0:
            t_h[k] += m[k]

    freq[(t_h[0], t_h[1])] = freq.get((t_h[0], t_h[1]), 0) + 1
    ans = max(ans, freq[(t_h[0], t_h[1])])

print(ans)