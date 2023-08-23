# problem link : https://www.codetree.ai/missions/5/problems/balance-on-coordinate-plane-2?&utm_source=clipboard&utm_medium=text

MAX_X = 100

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

ans = 100

for i in range(0, MAX_X + 1, 2):
    for j in range(0, MAX_X + 1, 2):
        segements = [0] * 5

        for x, y in points:
            if x > i and y > j:
                segements[1] += 1
            elif x < i and y > j:
                segements[2] += 1
            elif x < i and y < j:
                segements[3] += 1
            else:
                segements[4] += 1
        
        cur_m = max(segements)
        ans = min(ans, cur_m)

print(ans)