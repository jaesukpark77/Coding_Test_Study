# problem link : https://www.codetree.ai/missions/8/problems/top-k-frequent-elements?&utm_source=clipboard&utm_medium=text

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