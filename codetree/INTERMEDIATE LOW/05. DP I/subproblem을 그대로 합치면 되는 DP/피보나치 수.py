# proeblem link : https://www.codetree.ai/missions/2/problems/fibonacci-number?&utm_source=clipboard&utm_medium=text

# Backtracking method
n = int(input())

def fib(n):
    if n == 1 or n == 2:
        return 1

    return fib(n - 1) + fib(n - 2)

print(fib(n))

# DP (Memoization) method
n = int(input())

UNUSED = -1

memo = [UNUSED for _ in range(n + 1)]

def fib(n):
    if memo[n] != UNUSED:
        return memo[n]

    if n == 1 or n == 2:
        return 1
    
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

print(fib(n))

# DP (Tabulation) method
n = int(input())

MAX_NUM = 45

dp = [0 for _ in range(MAX_NUM + 1)]

dp[1] = dp[2] = 1

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])