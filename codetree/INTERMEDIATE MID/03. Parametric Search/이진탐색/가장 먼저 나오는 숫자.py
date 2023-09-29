# problem link : https://www.codetree.ai/missions/8/problems/first-appear-number?&utm_source=clipboard&utm_medium=text

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
queries = list(map(int, input().split()))

def lower_bound(target):
    left, right = 1, n
    min_idx = n + 1

    while left <= right:
        mid = (left + right) //  2

        if arr[mid] >= target:
            right = mid - 1
            min_idx = min(min_idx, mid)
        else:
            left = mid + 1
    
    return min_idx

for query in queries:
    lo = lower_bound(query)

    if lo <= n and arr[lo] == query:
        print(lo)
    else:
        print(-1)