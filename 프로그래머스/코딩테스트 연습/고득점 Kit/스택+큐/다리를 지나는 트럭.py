# problem link : https://school.programmers.co.kr/learn/courses/30/lessons/42583

# deque 활용

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    
    bridge = deque([0] * bridge_length)
    truck = deque(truck_weights)
    
    currentWeight = 0
    
    while len(truck) != 0:
        time += 1
        
        currentWeight -= bridge.popleft()
        
        if currentWeight + truck[0] <= weight:
            currentWeight += truck[0]
            bridge.append(truck.popleft())
        else:
            bridge.append(0)
    time += bridge_length
    return time

# stack 활용

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * (bridge_length)
    
    while bridge:
        answer += 1
        bridge.pop(0)
        
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                t = truck_weights.pop(0)
                bridge.append(t)
            else:
                bridge.append(0)
        
    return answer