from collections import deque

def solution(maps):
    answer = []
    que = deque()
    
    lx = len(maps[0])
    ly = len(maps)
    
    vis = [[False] * lx for _ in range(ly)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    plus = 0
    
    for i in range(ly):
        for j in range(lx):
            
            if maps[i][j] != 'X' and vis[i][j] == False:
                que.append((i, j))
                plus = 0
                while que:
                    
                    a = que.popleft()
                    plus += int(maps[a[0]][a[1]])
                    
                    vis[a[0]][a[1]] = True
                    for k in range(4):
                        plus_x = a[1]+dx[k]
                        plus_y = a[0]+dy[k]
                        if 0<=plus_x<=lx-1 and 0<=plus_y<=ly-1:
                            if vis[plus_y][plus_x]==False and maps[plus_y][plus_x] != 'X':
                                que.append((plus_y, plus_x))
                                vis[plus_y][plus_x] = True
                answer.append(plus)
    
    
    answer.sort()
    if answer:
        return answer
    else:
        answer.append(-1)
        return answer