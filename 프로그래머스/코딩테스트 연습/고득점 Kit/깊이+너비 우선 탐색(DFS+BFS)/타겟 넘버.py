# problem link : https://school.programmers.co.kr/learn/courses/30/lessons/43165

# BFS - deque method

from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    n = len(numbers)
    q.append([numbers[0], 0])
    q.append([-numbers[0], 0])
    while q:
        tmp, idx = q.popleft()
        idx += 1
        if idx < n:
            q.append([tmp + numbers[idx], idx])
            q.append([tmp - numbers[idx], idx])
        else:
            if tmp == target:
                answer += 1
    return answer

# BFS - list(stack) method

def solution(numbers, target):
    answer = 0
    queue = [[numbers[0],0], [-1*numbers[0],0]]
    n = len(numbers)
    while queue:
        temp, idx = queue.pop()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer

# DFS - 재귀함수 활용

def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    dfs(0,0)
    return answer