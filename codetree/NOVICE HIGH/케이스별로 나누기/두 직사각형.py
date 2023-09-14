# problem link : https://www.codetree.ai/missions/5/problems/two-rectangles?&utm_source=clipboard&utm_medium=text

x1, y1, x2, y2 = tuple(map(int, input().split()))
a1, b1, a2, b2 = tuple(map(int, input().split()))

def overlapping(x1, y1, x2, y2, a1, b1, a2, b2):
    if x2 < a1 or a2 < x1 or b2 < y1 or y2 < b1:
        return False
    else:
        return True

if overlapping(x1, y1, x2, y2, a1, b1, a2, b2):
    print("overlapping")
else:
    print("nonoverlapping")