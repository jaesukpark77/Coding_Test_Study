# problem link : https://www.codetree.ai/missions/8/problems/c-tag?&utm_source=clipboard&utm_medium=text

n, m = map(int, input().split())

A = [input() for _ in range(n)]
B = [input() for _ in range(n)]

ans = 0
s = set()

def test_location(x, y, z):
    s.clear()

    for i in range(n):
        s.add(A[i][x:x+1] + A[i][y:y+1] + A[i][z:z+1])

    for i in range(n):
        if (B[i][x:x + 1] + B[i][y:y + 1] + B[i][z:z + 1]) in s:
            return False
    
    return True

for i in range(m):
    for j in range(i+1, m):
        for k in range(j + 1, m):
            if test_location(i, j, k):
                ans += 1

print(ans)