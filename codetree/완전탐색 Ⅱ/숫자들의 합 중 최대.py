# problem link : https://www.codetree.ai/missions/5/problems/maximum-of-sum-of-numbers?utm_source=clipboard&utm_medium=text

x, y = tuple(map(int, input().split()))


def digit_sum(n):
    if n < 10:
        return n
    else:
        return digit_sum(n // 10) + (n % 10)


ans = 0

for i in range(x, y + 1):
    ans = max(ans, digit_sum(i))
    
print(ans)