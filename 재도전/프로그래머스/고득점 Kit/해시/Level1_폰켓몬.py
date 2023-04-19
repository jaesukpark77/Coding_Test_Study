def solution(nums):
  choose = len(nums) // 2
  nums = set(nums)
  answer = min(choose, len(nums))
  return answer

print(solution([3,1,2,3]))