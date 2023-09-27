# proeblem link : https://www.codetree.ai/missions/8/problems/count-number-of-points-2?&utm_source=clipboard&utm_medium=text

from sortedcontainers import SortedSet

MAX_M = 2000

n, q = map(int, input().split())
nums = SortedSet()
mapper = dict()
prefix_sum = [[0] * (MAX_M + 2) for _ in range(MAX_M + 2)]

points = [tuple(map(int, input().split())) for _ in range(n)]

queries = [tuple(map(int, input().split())) for _ in range(q)]

def get_lower_boundary(x):
    return nums.bisect_left(x) + 1

def get_upper_boundary(x):
    return nums.bisect_right(x)

def get_sum(x1, y1, x2, y2):
    return prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1]

for x, y in points:
    nums.add(x)
    nums.add(y)

cnt = 1
for num in nums:
    mapper[num] = cnt
    cnt += 1

for x, y in points:
    new_x, new_y = mapper[x], mapper[y]
    prefix_sum[new_x][new_y] += 1

for i in range(1, cnt + 1):
    for j in range(1, cnt + 1):
        prefix_sum[i][j] += prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

for x1, y1, x2, y2 in queries:
    new_x1 = get_lower_boundary(x1)
    new_y1 = get_lower_boundary(y1)
    new_x2 = get_upper_boundary(x2)
    new_y2 = get_upper_boundary(y2)

    ans = get_sum(new_x1, new_y1, new_x2, new_y2)
    
    print(ans)