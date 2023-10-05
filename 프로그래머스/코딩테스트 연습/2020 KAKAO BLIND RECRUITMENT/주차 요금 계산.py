# 해시 테이블
# problem link : https://school.programmers.co.kr/learn/courses/30/lessons/92341?language=python3

import math

def solution(fees, records):
    in_car = dict()
    out_car = dict()
    
    for x in records:
        t, n, v = x.split()
        h, m = t.split(':')
        time = int(h) * 60 + int(m)
        
        if v == 'IN':
            in_car[n] = time
        else:
            out_car[n] = out_car.get(n, 0) + time - in_car[n]
            del in_car[n]
    
    for x in in_car:
        out_car[x] = out_car.get(x, 0) + (23 * 60 + 59) - in_car[x]
        
    answer = []
    
    for num, fee in sorted(out_car.items()):
        if fee > fees[0]:
            answer.append(fees[1] + math.ceil((fee - fees[0]) / fees[2]) * fees[3])
        else:
            answer.append(fees[1])
    return answer