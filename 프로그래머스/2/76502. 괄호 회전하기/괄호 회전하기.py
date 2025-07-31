from collections import deque

def solution(s):
    start = ['[', '{', '(']
    end = [']', '}', ')']
    answer = 0
    
    first_s = list(s)
    for _ in range(len(s)):
        
        s = deque(first_s)
        que = deque()
        que.append(s.popleft())

        for i in range(len(s)):
            temp = s.popleft()
            if temp in start:
                que.append(temp)
            else:
                if len(que)!= 0 and (que[-1] in start) and (end.index(temp) == start.index(que[-1])):
                    que.pop()
                else:
                    break
        if len(que) == 0 and len(s) == 0:
            answer += 1
        first_s.append(first_s.pop(0))
                
    
    return answer