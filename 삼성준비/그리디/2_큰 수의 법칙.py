# solve 1
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
#
# data.sort()
# first = data[-1]
# second = data[-2]
#
# result = 0
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1
#
# print(result)

# solve 2
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[-1]
second = data[-2]

count = (m // (k+1)) * k
count += m % (k+1)

result = 0
result += count * first
result += (m-count) * second
print(result)