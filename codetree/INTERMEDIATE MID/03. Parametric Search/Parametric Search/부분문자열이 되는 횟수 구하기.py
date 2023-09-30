# problem link : https://www.codetree.ai/missions/8/problems/find-the-number-of-partial-strings?&utm_source=clipboard&utm_medium=text

a = input()
b = input()
delete = list(map(int, input().split()))

n = len(a)
m = len(b)
skip = [False] * n

def is_possible(mid):
    b_idx = 0

    for i in range(mid):
        skip[delete[i] - 1] = True
    
    for i in range(n):
        if skip[i]:
            continue
        if b_idx < m and a[i] == b[b_idx]:
            b_idx += 1
    
    return b_idx == m

lo = 0
hi = n
ans = -1

while lo <= hi:
    mid = (lo + hi) // 2
    if is_possible(mid):
        lo = mid + 1
        ans = max(ans, mid)
    else:
        hi = mid - 1

    for i in range(mid):
        skip[delete[i] - 1] = False

print(ans + 1)