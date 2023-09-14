n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n)]

def area(x1, y1, x2, y2, x3, y3):
    return abs ((x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3))

max_area = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]
            if (x1 == x2 or x1 == x3 or x2 == x3) and (y1 == y2 or y1 == y3 or y2 == y3):
                max_area = max(max_area, area(x1, y1, x2, y2, x3, y3))

print(max_area)