# problem link : https://www.codetree.ai/missions/5/problems/tic-tac-to-as-a-team-2?&utm_source=clipboard&utm_medium=text

MAX_A = 3
MAX_X = 9

board = [list(map(int, input())) for _ in range(MAX_A)]

ans = 0

for i in range(1, MAX_X + 1):
    for j in range(i+1, MAX_X + 1):
        win = False

        num_i = 0
        num_j = 0

        for k in range(MAX_A):
            num_i = 0
            num_j = 0

            for l in range(MAX_A):
                if board[k][l] == i:
                    num_i += 1
                if board[k][l] == j:
                    num_j += 1
            
            if num_i + num_j == 3 and num_i >= 1 and num_j >= 1:
                win = True

        for k in range(MAX_A):
            num_i = 0
            num_j = 0

            for l in range(MAX_A):
                if board[l][k] == i:
                    num_i += 1
                if board[l][k] == j:
                    num_j += 1
            
            if num_i + num_j == 3 and num_i >= 1 and num_j >= 1:
                win = True

        num_i = 0
        num_j = 0

        for k in range(MAX_A):
            if board[k][k] == i:
                num_i += 1
            if board[k][k] == j:
                num_j += 1

        if num_i + num_j == 3 and num_i >= 1 and num_j >= 1:
            win = True
        
        num_i = 0
        num_j = 0

        for k in range(MAX_A):
            if board[k][MAX_A - k - 1] == i:
                num_i += 1
            if board[k][MAX_A - k - 1] == j:
                num_j += 1

        
        if num_i + num_j == 3 and num_i >= 1 and num_j >= 1:
            win = True

        if win:
            ans += 1

print(ans)
