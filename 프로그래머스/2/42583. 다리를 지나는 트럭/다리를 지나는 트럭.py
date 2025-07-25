## 꼼수 쓰려다 2시간 날림.

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    b_w = 0
    
    while len(truck_weights):
        truck = truck_weights[0]
        a= bridge.pop()
        b_w -= a
        
        if truck+b_w <= weight:
            bridge.appendleft(truck)
            b_w += truck
            truck_weights.popleft()
        else:
            bridge.appendleft(0)
        answer+=1

    answer += bridge_length
            
    return answer