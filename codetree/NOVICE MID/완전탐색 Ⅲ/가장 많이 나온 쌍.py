# problem link : https://www.codetree.ai/missions/5/problems/the-most-frequent-pair?&utm_source=clipboard&utm_medium=text

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

def count_num(first, second):
    cnt = 0
    for a, b in points:
        if (first, second) in [(a, b), (b, a)]:
            cnt += 1

    return cnt

ans = 0

for i in range(1, n+1):
    for j in range(i+1, n + 1):
        ans = max(ans, count_num(i, j))

print(ans)