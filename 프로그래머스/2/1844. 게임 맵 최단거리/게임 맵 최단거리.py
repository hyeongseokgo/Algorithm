from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append((0, 0, 1))  

    while queue:
        x, y, dist = queue.popleft()

        if x == m - 1 and y == n - 1:
            return dist

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1:
                maps[ny][nx] = 0 
                queue.append((nx, ny, dist + 1)) 

    return -1
