from collections import deque

N, K = map(int, input().split())
yose = deque(range(1, N + 1))
answer = []

while yose:
    yose.rotate(-(K - 1))
    answer.append(yose.popleft())
    
print("<" + ", ".join(map(str, answer)) + ">")