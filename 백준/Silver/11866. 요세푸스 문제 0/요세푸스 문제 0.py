from collections import deque

N, K = map(int, input().split())
yose = list(range(1, N + 1))
answer = []
idx = 0

while yose:
    idx = (idx + K - 1) % len(yose)
    answer.append(yose.pop(idx))
    
print("<" + ", ".join(map(str, answer)) + ">")