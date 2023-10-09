# problem link : https://www.codetree.ai/missions/8/problems/top-k-frequent-elements?&utm_source=clipboard&utm_medium=text

# solution 1

n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = dict()

for elem in arr:
    if elem in count:
        count[elem] += 1
    else:
        count[elem] = 1

new_arr = [[value, key] for key, value in count.items()]

new_arr = sorted(new_arr)

leng = len(new_arr)
for i in range(leng - 1, leng - k - 1, -1):
    print(new_arr[i][1], end = ' ')

# solution 2

from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = defaultdict(lambda: 0)

for elem in arr:
    count[elem] += 1

new_arr = [[value, key] for key, value in count.items()]
new_arr.sort()

final_arr = new_arr[::-1]
for i in range(k):
    print(final_arr[i][1], end=' ')


# soultion 3

from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

count = defaultdict(lambda: 0)

for elem in arr:
    count[elem] += 1

# value 순으로 정렬, 그 안에서 key순으로 정렬해야함.
# 그 이후, k개 빼내면 됨

count = dict(sorted(count.items(), key=lambda x:(-x[1], -x[0])))
keys = list(count.keys())
for i in range(k):
    print(keys[i], end=' ')