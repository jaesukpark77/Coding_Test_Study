# problem link : https://www.codetree.ai/missions/8/problems/data-comparison?&utm_source=clipboard&utm_medium=text

n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

set1 = set(arr1)

for elem2 in arr2:
    if elem2 not in set1:
        print(0, end=' ')
    else:
        print(1, end=' ')
