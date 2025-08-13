from collections import deque

def solution(x, y, n):
    answer = -1
    
    vis = set([x])
    time = 0
    
    que = deque([(x,time)])
    
    
    while que:
        a, ti = que.popleft()
        if a == y:
            answer = ti
            break
        
        for i in [a*2, a*3, a+n]:
            if i <= y and i not in vis:
                vis.add(i)
                que.append((i, ti+1))
        
    return answer