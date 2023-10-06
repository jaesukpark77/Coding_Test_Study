# problem link : https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = []
    
    for i in number:
        if len(answer) == 0:
            answer.append(i)
            continue
        if k > 0:
            while answer[-1] < i:
                answer.pop()
                k -= 1
                if len(answer) == 0 or k <= 0:
                    break
        answer.append(i)
        
    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)