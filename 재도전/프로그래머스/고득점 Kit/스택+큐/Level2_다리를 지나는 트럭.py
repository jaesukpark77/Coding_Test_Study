from collections import deque

def solution(bridge_length, weight, truck_weights):
  answer = 0
  truck_bridge_deque = deque(bridge_length * [0])
  truck_weights_deque = deque(truck_weights)
  while len(truck_bridge_deque):
    answer += 1
    truck_bridge_deque.popleft()
    if truck_weights_deque:
      if sum(truck_bridge_deque) + truck_weights_deque[0] <= weight:
        truck_bridge_deque.append(truck_weights_deque.popleft())
      else:
        truck_bridge_deque.append(0)

  return answer

print(solution(100, 100, [10]))