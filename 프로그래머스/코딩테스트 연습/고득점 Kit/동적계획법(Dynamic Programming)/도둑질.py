# problem link : https://school.programmers.co.kr/learn/courses/30/lessons/42897

def solution(money):
    dp = [0] * len(money)
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    
    for i in range(2, len(money) - 1):
        dp[i] = max(dp[i-1], money[i] + dp[i-2])
        
    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]
    
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], money[i]+dp2[i-2])
    return max(max(dp), max(dp2))