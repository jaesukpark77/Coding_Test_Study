# problem link : https://school.programmers.co.kr/learn/courses/30/lessons/43105

# solution 1

def solution(triangle):
    leng = len(triangle)
    dp = [[0] * leng for _ in range(leng)]
    dp[0][0] = triangle[0][0]
    
    for i in range(leng - 1):
        for j in range(len(triangle[i])):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + triangle[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + triangle[i+1][j+1])
    
    return max(dp[-1])

# solution 2

def solution(triangle):
    # 뒤에서부터 역순으로 DP 테이블 초기화
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # 아래층의 두 수 중 큰 값을 현재 칸의 값에 더함
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    return triangle[0][0]