# problem link : https://www.codetree.ai/missions/2/problems/make-one-using-four-operations?&utm_source=clipboard&utm_medium=text

from collections import deque
import math
from enum import Enum

OPERATOR_NUM = 4
INT_MAX = math.inf

class OPERATOR(Enum):
    SUBTRACT = 0
    ADD = 1
    DIV2 = 2
    DIV3 = 3

n = int(input())
ans = INT_MAX

q = deque()
vistited = [False for _ in range(2 * n)]
step = [0 for _ in range(2 * n)]

def possible(num, op):
    if op == OPERATOR.SUBTRACT.value or op == OPERATOR.ADD.value:
        return True
    elif op == OPERATOR.DIV2.value:
        return num % 2 == 0
    else:
        return num % 3 == 0

def calculate(num, op):
    if op == OPERATOR.SUBTRACT.value:
        return num - 1
    elif op == OPERATOR.ADD.value:
        return num + 1
    elif op == OPERATOR.DIV2.value:
        return num // 2
    else:
        return num // 3

def in_range(num):
    return 1 <= num and num < 2 * n

def can_go(num):
    return in_range(num) and not vistited[num]

def push(num, new_step):
    q.append(num)
    vistited[num] = True
    step[num] = new_step

def find_min():
    global ans

    while q:
        curr_num = q.popleft()

        for i in range(OPERATOR_NUM):
            if not possible(curr_num, i):
                continue
            
            new_num = calculate(curr_num, i)
            if can_go(new_num):
                push(new_num, step[curr_num] + 1)

        ans = step[1]

push(n, 0)
find_min()
print(ans)