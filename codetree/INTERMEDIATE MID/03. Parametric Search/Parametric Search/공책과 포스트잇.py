# problem link : https://www.codetree.ai/missions/8/problems/note-and-sticky-note?&utm_source=clipboard&utm_medium=text

n, k, l = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

def is_possible(h):
    cnt = 0
    for i in range(n - h, n):
        if arr[i] < h:
            cnt += h - arr[i]

    return cnt <= k * l and arr[n - h] + k >= h

arr.sort()

left = -1
right = n
ans = 0

while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        left = mid + 1
        ans = max(ans, mid)
    else:
        right = mid - 1

print(ans)