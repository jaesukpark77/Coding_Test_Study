# 이분 탐색
# problem link : https://school.programmers.co.kr/learn/courses/30/lessons/64062

def solution(stones, k):
    left = 1
    right = 200000000
    while left <= right:
        temp = stones.copy()
        mid = (left + right) // 2
        
        cnt = 0
        
        for t in temp:
            if t - mid <= 0:
                cnt += 1
            else:
                cnt = 0 # 0이 연속적으로 나오지않았으면 다시 초기화 진행
                
            if cnt >= k:
                break
                
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1
            
    return left