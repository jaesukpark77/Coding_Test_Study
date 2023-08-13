# 문제 링크 : https://www.codetree.ai/missions/5/problems/rotten-cheese?utm_source=clipboard&utm_medium=text

class Info1:
    def __init__(self, p, m, t):
        self.p, self.m, self.t = p, m, t

class Info2:
    def __init__(self, p, t):
        self.p, self.t = p, t

n, m, d, s = map(int, input().split())

info1 = []
for _ in range(d):
    p, m, t = tuple(map(int, input().split()))
    info1.append(Info1(p, m, t))

info2 = []
for _ in range(s):
    p, t = tuple(map(int, input().split()))
    info2.append(Info2(p, t))

ans = 0

for i in range(1, m+1):
    time = [0] * (n+1)
    for info in info1:
        if info.m != i:
            continue
        
        person = info.p
        if time[person] == 0:
            time[person] = info.t
        elif time[person] > info.t:
            time[person] = info.t
        
    possible = True

    for info in info2:
        person = info.p
        if time[person] == 0:
            possible = False
        if time[person] >= info.t:
            possible = False
    
    pill = 0
    if possible:
        for j in range(1, n+1):
            if time[j] != 0:
                pill += 1
    
    ans = max(ans, pill)

print(ans)