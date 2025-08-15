from collections import deque

def solution(ingredient):
    answer = 0
    stack = deque()
    
    for i in ingredient:
        stack.append(i)
        if len(stack) >= 4 and [stack[-1], stack[-2], stack[-3], stack[-4]] == [1, 3, 2, 1]:
            answer += 1
            for j in range(4):  stack.pop()
            
    
    
    
    
    return answer