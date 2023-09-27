# problem link : https://www.codetree.ai/missions/8/problems/the-number-of-points-within-the-range-2?&utm_source=clipboard&utm_medium=text

n, q = map(int, input().split())
points = list(map(int, input().split()))
query = [tuple(map(int, input().split())) for _ in range(q)]

MAX_A = 1000000
prefix_sum = [0] * (MAX_A + 1)

for point in points:
    prefix_sum[point] += 1

for i in range(1, MAX_A + 1):
    prefix_sum[i] += prefix_sum[i - 1]

def get_sum(s, e):
    if s == 0:
        return prefix_sum[e]
    return prefix_sum[e] - prefix_sum[s - 1]

for (l, r) in query:
    print(get_sum(l, r))