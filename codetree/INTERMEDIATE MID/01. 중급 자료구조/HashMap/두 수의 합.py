# problem link : https://www.codetree.ai/missions/8/problems/sum-of-two-num?&utm_source=clipboard&utm_medium=text

n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = dict()

ans = 0

for elem in arr:
    diff = k - elem

    if diff in count:
        ans += count[diff]

    if elem in count:
        count[elem] += 1
    else:
        count[elem] = 1

print(ans)