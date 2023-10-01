# problem link : https://www.codetree.ai/missions/8/problems/implement-scheduling-meeting-room?&utm_source=clipboard&utm_medium=text

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

meetings.sort(key = lambda x: x[1])

last_e, ans = -1, 0
for s, e in meetings:
    if last_e <= s:
        last_e = e
        ans += 1

print(ans)