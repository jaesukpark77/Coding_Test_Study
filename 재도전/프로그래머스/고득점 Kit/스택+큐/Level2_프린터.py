def solution(priorities, location):
  printer = [(i, p) for i, p in enumerate(priorities)]
  turn = 0
  while printer:
    job = printer.pop(0)
    if any(job[1] < other_job[1] for other_job in printer):
      printer.append(job)
    else:
      turn += 1
      if job[0] == location:
        break
  return printer

print(solution([2, 1, 3, 2], 2))