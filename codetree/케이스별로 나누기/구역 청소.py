# problem link : https://www.codetree.ai/missions/5/problems/district-cleaning?&utm_source=clipboard&utm_medium=text

a, b = map(int, input().split())
c, d = map(int, input().split())

def intersecting(x1, x2, x3, x4):
    if x2 < x3 or x4 < x1:
        return False
    else:
        return True

if intersecting(a, b, c, d):
    print(max(b, d) - min(a, c))
else:
    print((b - a) + (d - c))