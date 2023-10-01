# problem link : https://www.codetree.ai/missions/8/problems/fill-in-number?&utm_source=clipboard&utm_medium=text

MAX_NUM = 100000

n = int(input())
ans = MAX_NUM

for i in range(MAX_NUM + 1):
    remainder = n - 5 * i
    if remainder >= 0 and remainder % 2 == 0:
        ans = min(ans, i + (remainder // 2))

if ans == MAX_NUM:
    ans = -1

print(ans)