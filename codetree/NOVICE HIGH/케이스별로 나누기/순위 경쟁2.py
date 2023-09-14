# problem link : https://www.codetree.ai/missions/5/problems/ranking-competition2?&utm_source=clipboard&utm_medium=text

n = int(input())

changes = [input().split() for _ in range(n)]

score_a, score_b = 0, 0

def get_status(score1, score2):
    if score1 > score2:
        return 1
    elif(score2 > score1):
        return 2
    else:
        return 3

ans = 0

for name, value in changes:
    value = int(value)

    if name == 'A':
        if get_status(score_a, score_b) != get_status(score_a + value, score_b):
            ans += 1
        
        score_a += value
    else:
        if get_status(score_a, score_b) != get_status(score_a, score_b + value):
            ans += 1
        
        score_b += value

print(ans)