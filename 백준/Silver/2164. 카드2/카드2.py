from collections import deque
num = int(input())
card = deque([x+1 for x in range(num)])

while len(card) != 1:
    card.popleft()
    a = card.popleft()
    card.append(a)

print(card[0])