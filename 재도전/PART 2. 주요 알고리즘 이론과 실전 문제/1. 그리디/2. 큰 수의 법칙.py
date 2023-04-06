# solution 1
""" n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0]
second = data[1]

result = 0

while True:
  for i in range(k):
    if m == 0:
      break
    result += first
    m -= 1
  if m == 0:
    break
  result += second
  m -= 1

print(result) """

# solution 2
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0]
second = data[1]

count = ((m//(k+1)) * k) + (m % (k+1))

result = (count * first) + ((m-count) * second)

print(result)