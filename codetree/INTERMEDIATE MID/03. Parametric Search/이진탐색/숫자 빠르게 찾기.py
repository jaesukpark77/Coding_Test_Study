# problem link : https://www.codetree.ai/missions/8/problems/find-number-fast?&utm_source=clipboard&utm_medium=text

n, m = map(int, input().split())
arr = list(map(int, input().split()))

def find_target(target):
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        
        if arr[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

for _ in range(m):
    x = int(input())
    index = find_target(x)

    print(-1 if index < 0 else index + 1)