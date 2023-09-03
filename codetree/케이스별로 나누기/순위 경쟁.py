# problem link : https://www.codetree.ai/missions/5/problems/ranking-competition?&utm_source=clipboard&utm_medium=text

n = int(input())

changes = [input().split() for _ in range(n)]

score_a, score_b, score_c = 0, 0, 0

def get_status(score1, score2, score3):
    return_val = 0
    maxval = max([score1, score2, score3])

    if score1 == maxval:
        return_val += 1

    if score2 == maxval:
        return_val += 2
    
    if score3 == maxval:
        return_val += 4
    
    return return_val

ans = 0

for name, value in changes:
    value = int(value)
    if name == 'A':
        if get_status(score_a, score_b, score_c) != get_status(score_a + value, score_b, score_c):
            ans += 1       
        score_a += value
    elif name == 'B':
        if get_status(score_a, score_b, score_c) != get_status(score_a, score_b + value, score_c):
            ans += 1
        score_b += value
    else:
        if get_status(score_a, score_b, score_c) != get_status(score_a, score_b, score_c + value):
            ans += 1
        score_c += value

print(ans)