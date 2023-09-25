# problem link : https://www.codetree.ai/missions/2/problems/longest-common-sequence?&utm_source=clipboard&utm_medium=text

str1 = input()
str2 = input()

str1_len, str2_len = len(str1), len(str2)
str1, str2 = '#' + str1, '#' + str2

dp = [
    [0 for _ in range(str2_len + 1)]
    for _ in range(str1_len + 1)
]

def initialize():
    dp[1][1] = int(str1[1] == str2[1])

    for i in range(2, str1_len + 1):
        if str1[i] == str2[1]:
            dp[i][1] = 1
        else:
            dp[i][1] = dp[i-1][1]
    
    for j in range(2, str2_len + 1):
        if str1[1] == str2[j]:
            dp[1][j] = 1
        else:
            dp[1][j] = dp[1][j-1]
            
initialize()

for i in range(2, str1_len + 1):
    for j in range(2, str2_len + 1):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
print(dp[str1_len][str2_len])