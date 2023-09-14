# problem link : https://www.codetree.ai/missions/5/problems/study-cafe-keeping-distance-4?&utm_source=clipboard&utm_medium=text

n = int(input())
seat = list(input())

def min_seat():
    dist = n
    for i in range(n):
        for j in range(i+1, n):
            if seat[i] == '1' and seat[j] == '1':
                dist = min(dist, j - i)
    
    return dist

ans = 0
for i in range(n):
    for j in range(i+1, n):
        if seat[i] == '0' and seat[j] == '0':
            seat[i] = seat[j] = '1'
            ans = max(ans, min_seat())
            seat[i] = seat[j] = '0'

print(ans)