# problem link : https://school.programmers.co.kr/learn/courses/30/lessons/60061

# set 방식 활용

def impossible(result):
    COL, ROW = 0, 1
    for x, y, a in result:
        if a == COL:
            if y != 0 and (x, y - 1, COL) not in result and (x - 1, y, ROW) not in result and (x, y, ROW) not in result:
                return True
        else:
            if (x, y - 1, COL) not in result and (x + 1, y - 1, COL) not in result and not((x - 1, y, ROW) in result and (x + 1, y, ROW) in result):
                return True
    return False


def solution(n, build_frame):
    result = set()
    
    for x, y, a, b in build_frame:
        item = (x, y, a)
        
        if b:
            result.add(item)
            if impossible(result):
                result.remove(item)
        elif item in result:
            result.remove(item)
            if impossible(result):
                result.add(item)
    
    answer = list(result)
    answer.sort(key = lambda x: (x[0], x[1], x[2]))
    return answer

# array 방식 활용

def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: #기둥 체크
            #'바닥 위' or '보의 한쪽 끝 위' or '또 다른 기둥 위' 
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif stuff == 1: #보 체크
            #'한쪽 끝 부분이 기둥 위' or '양쪽 끝 부분이 다른 보와 동시 연결'
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for build in build_frame:
        x, y, stuff, operation = build
        
        if operation == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
        elif operation == 0:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
    answer.sort(key = lambda x : (x[0], x[1], x[2]))
    return answer