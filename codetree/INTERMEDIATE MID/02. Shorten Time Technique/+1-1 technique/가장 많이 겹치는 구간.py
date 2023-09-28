# problem link : https://www.codetree.ai/missions/8/problems/section-with-maximum-overlap?&utm_source=clipboard&utm_medium=text

MAX_R = 200000

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
checked = [0] * (MAX_R + 1)
ans = 0

for x1, x2 in segments:
    checked[x1] += 1
    checked[x2] -= 1

overlapped_cnt = 0

for x in range(1, MAX_R + 1):
    overlapped_cnt += checked[x]
    ans = max(ans, overlapped_cnt)
    
print(ans)