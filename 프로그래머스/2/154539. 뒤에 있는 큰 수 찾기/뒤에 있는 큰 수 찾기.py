from collections import deque

def solution(numbers):
    answer = []
    stack = deque()
    
    for i in range(len(numbers)-1,-1,-1):
        while len(stack) != 0:
            if stack[-1] <= numbers[i]:
                stack.pop()
            else:
                stack.append(numbers[i])
                numbers[i] = stack[-2]
                break
        if len(stack) == 0:
            stack.append(numbers[i])
            numbers[i] = -1
        
    
    return numbers