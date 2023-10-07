# problem link : https://www.codetree.ai/missions/2/problems/The-1D-wind-blows?&utm_source=clipboard&utm_medium=text

SHIFT_RIGHT = 0
SHIFT_LEFT = 1

n, m, q = map(int, input().split())
arr = [[0] * (m + 1) for _ in range(n + 1)]

def shift(row, curr_dir):
    if curr_dir == SHIFT_RIGHT:
        arr[row].insert(1, arr[row].pop())
    else:
        arr[row].insert(m, arr[row].pop(1))

def has_same_number(row1, row2):
    return any([
        arr[row1][col] == arr[row2][col]
        for col in range(1, m + 1)
    ])

def flip(curr_dir):
    return SHIFT_RIGHT if curr_dir == SHIFT_LEFT else SHIFT_LEFT

def simulate(start_row, start_dir):
    # Step1
    # 바람이 처음으로 불어 온 행의 숫자들을 해당 방향으로 밀어줍니다.
    shift(start_row, start_dir)
    
    # 그 이후부터는 반전된 방향에 영향을 받으므로, 방향을 미리 반전시켜 줍니다.
    start_dir = flip(start_dir)
    
    # Step2
    # 위 방향으로 전파를 계속 시도해봅니다.
    curr_dir = start_dir
    for row in range(start_row, 1, -1):
        # 인접한 행끼리 같은 숫자를 가지고 있다면
        # 위의 행을 한 칸 shift 하고
        # 방향을 반대로 바꿔 계속 전파를 진행합니다.
        if has_same_number(row, row - 1):
            shift(row - 1, curr_dir)
            curr_dir = flip(curr_dir)
        # 같은 숫자가 없다면 전파를 멈춥니다.
        else:
            break
    
    # Step3
    # 아래 방향으로 전파를 계속 시도해봅니다.
    curr_dir = start_dir
    for row in range(start_row, n):
        # 인접한 행끼리 같은 숫자를 가지고 있다면
        # 아래 행을 한 칸 shift하고
        # 방향을 반대로 바꿔 계속 전파를 진행합니다.
        if has_same_number(row, row + 1):
            shift(row + 1, curr_dir)
            curr_dir = flip(curr_dir)
        # 같은 숫자가 없다면 전파를 멈춥니다.
        else:
            break

for row in range(1, n + 1):
    given_nums = list(map(int, input().split()))
    for col, num in enumerate(given_nums, start = 1):
        arr[row][col] = num

for _ in range(q):
    r, d = tuple(input().split())
    r = int(r)
    
    simulate(r, SHIFT_RIGHT if d == 'L' else SHIFT_LEFT)

for row in range(1, n + 1):
    for col in range(1, m + 1):
        print(arr[row][col], end = " ")
    print()