def solution(phone_book):
  d = {}
  for x in phone_book:
    d[x] = d.get(x, 0) + 1
  for x in phone_book:
    s = ''
    for num in x:
      s += num
      if s in d and s != x:
        return False
  return True

print(solution(["119", "97674223", "1195524421"]))