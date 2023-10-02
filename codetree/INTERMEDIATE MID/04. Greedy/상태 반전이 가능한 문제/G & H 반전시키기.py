# problem link : https://www.codetree.ai/missions/8/problems/reversing-g-and-h?&utm_source=clipboard&utm_medium=text

n = int(input())
a = input()
b = input()

ans = 0
mismatched = False

for i in range(n):
    if a[i] != b[i]:
        if not mismatched:
            mismatched = True
            ans += 1
    else:
        mismatched = False

print(ans)