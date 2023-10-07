# problem link : https://www.codetree.ai/missions/2/problems/non-overlapping-two-rectangles?&utm_source=clipboard&utm_medium=text

import math

INT_MIN = -math.inf

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# 두 직사각형이 겹쳐지는지에 대한 여부 판단 위한 배열
board = [[0] * m for _ in range(n)]

# 판단 위한 배열 초기화
def clear_board():
    for i in range(n):
        for j in range(m):
            board[i][j] = 0

# 판단 위한 배열 위치 여부 판단
def draw(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            board[i][j] += 1

# 판단 위한 배열 겹치는 지 판단
def check_board():
    for i in range(n):
        for j in range(m):
            if board[i][j] >= 2:
                return True
    return False

def overlap(x1, y1, x2, y2, x3, y3, x4, y4):
    clear_board()
    draw(x1, y1, x2, y2)
    draw(x3, y3, x4, y4)

    return check_board()

# 합 구하기
def rect_sum(x1, y1, x2, y2):
    return sum([
        grid[i][j] 
        for i in range(x1, x2 + 1) 
        for j in range(y1, y2 + 1)
    ])

# 첫 번째 직사각형이 (x1, y1), (x2, y2)를 양쪽 꼭지점으로 할 때 두 번째 직사각형을 겹치지 않게 잘 잡아 최대 합을 반환하는 함수
def find_max_sum_with_rect(x1, y1, x2, y2):
    max_sum = INT_MIN

    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    if not overlap(x1, y1, x2, y2, i, j, k, l):
                        max_sum = max(max_sum, rect_sum(x1, y1, x2, y2) + rect_sum(i, j, k, l))

    return max_sum

# 두 직사각형을 잘 잡았을 때의 최대 합을 반환하는 함수
def find_max_sum():
    max_sum = INT_MIN

    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    max_sum = max(max_sum, find_max_sum_with_rect(i, j, k, l))

    return max_sum

ans = find_max_sum()
print(ans)