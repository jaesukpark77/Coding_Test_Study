# problem link : https://www.codetree.ai/missions/5/problems/two-lines?&utm_source=clipboard&utm_medium=text

x1, x2, x3, x4 = tuple(map(int, input().split()))

def intersect(x1, x2, x3, x4):
    if x2 < x3 or x4 < x1:
        return False
    else:
        return True

if intersect(x1, x2, x3, x4):
    print("intersecting")
else:
    print("nonintersecting")