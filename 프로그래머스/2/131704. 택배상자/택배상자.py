from collections import deque

def solution(order):
    count = 0
    sub = deque()
    box = 1
    
    for i in order:
        if i >= box:
            for j in range(i-box):
                sub.append(box)
                box += 1
            box+= 1
            count+=1
        elif i < box:
            if sub[-1] == i:
                sub.pop()
                count+= 1
            else:
                break
            
    return count