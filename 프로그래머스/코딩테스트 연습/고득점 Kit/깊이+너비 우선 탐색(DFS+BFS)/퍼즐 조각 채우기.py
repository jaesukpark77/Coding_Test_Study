# problem link : https://school.programmers.co.kr/learn/courses/30/lessons/84021

from collections import deque

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs(i, j, table, check):
    puzzle = []
    n = len(table)
    q = deque()
    q.append((i, j))
    check[i][j] = True
    
    def in_range(x, y):
        return 0 <= x and x < n and 0 <= y and y < n
    
    while q:
        x, y = q.popleft()
        puzzle.append([x, y])
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if in_range(nx, ny) and not check[nx][ny] and table[nx][ny] == 1:
                q.append((nx, ny))              
                check[nx][ny] = True
                
    return puzzle
    
def trans_puzzle(puzzle_location):
    r_min, r_max = 100, -1
    c_min, c_max = 100, -1
    
    for location in puzzle_location:
        r, c = location
        r_min = min(r_min, r)
        r_max = max(r_max, r)
        c_min = min(c_min, c)
        c_max = max(c_max, c)
        
    r_len = r_max - r_min + 1
    c_len = c_max - c_min + 1
    
    trans = [[0] * c_len for _ in range(r_len)]
    
    for location in puzzle_location:
        x = location[0] - r_min
        y = location[1] - c_min
        trans[x][y] = 1
        
    return trans

def rotation(puzzle):
    n = len(puzzle)
    m = len(puzzle[0])
    result = [[0] * n for _ in range(m)]
    for r in range(n):
        for c in range(m):
            result[c][n - r - 1] = puzzle[r][c]
            
    return result

def empty_side(game_board, puzzle, i, j):
    n = len(game_board)
    
    def in_range(x, y):
        return 0 <= x and x < n and 0 <= y and y < n
    
    for x in range(len(puzzle)):
        for y in range(len(puzzle[0])):
            if puzzle[x][y] == 1:
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + i + dx, y + j + dy
                    
                    if in_range(nx, ny) and game_board[nx][ny] != 1:
                        return True
                    
    return False
                    
def is_match(puzzle, game_board):
    n = len(game_board)
    r = len(puzzle)
    c = len(puzzle[0])
    
    for i in range(n - r + 1):
        for j in range(n-c+1):
            match = True
            for x in range(len(puzzle)):
                for y in range(len(puzzle[0])):
                    game_board[x+i][y+j] += puzzle[x][y]
                    if game_board[x+i][y+j] != 1:
                        match = False

            if empty_side(game_board, puzzle, i, j):
                match = False

            if match:
                return True
            else:
                for x in range(len(puzzle)):
                    for y in range(len(puzzle[0])):
                        game_board[x+i][y+j] -= puzzle[x][y]

    return False

def solution(game_board, table):
    n = len(game_board)
    answer = 0
    puzzles = []
    check = [[False] * n for _ in range(n)]
    puzzle_sum = []
    
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and not check[i][j]:
                puzzle_location = bfs(i, j, table, check)
                puzzle = trans_puzzle(puzzle_location)
                puzzles.append(puzzle)
                puzzle_sum.append(len(puzzle_location))
                
    for idx, puzzle in enumerate(puzzles):
        for _ in range(4):
            puzzle = rotation(puzzle)
            if is_match(puzzle, game_board):
                answer += puzzle_sum[idx]
                break
                
    return answer