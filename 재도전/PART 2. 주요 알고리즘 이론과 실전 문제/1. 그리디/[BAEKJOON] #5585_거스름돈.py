remain = 1000 - int(input())
coin_list = [500, 100, 50, 10, 5, 1]

count = 0
for coin in coin_list:
  count += remain // coin
  remain %= coin

print(count)