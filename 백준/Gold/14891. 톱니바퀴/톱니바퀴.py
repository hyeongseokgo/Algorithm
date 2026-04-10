from collections import deque

gears = [deque(map(int, input().strip())) for _ in range(4)]

k = int(input())

def rotate(idx, direction):
    if direction == 1:
        gears[idx].rotate(1)
    elif direction == -1:
        gears[idx].rotate(-1)

for _ in range(k):
    num, direction = map(int, input().split())
    num -= 1

    rotate_dir = [0] * 4
    rotate_dir[num] = direction

    for i in range(num, 0, -1):
        if gears[i][6] != gears[i - 1][2]:
            rotate_dir[i - 1] = -rotate_dir[i]
        else:
            break

    for i in range(num, 3):
        if gears[i][2] != gears[i + 1][6]:
            rotate_dir[i + 1] = -rotate_dir[i]
        else:
            break

    for i in range(4):
        if rotate_dir[i] != 0:
            rotate(i, rotate_dir[i])


score = 0
if gears[0][0] == 1:
    score += 1
if gears[1][0] == 1:
    score += 2
if gears[2][0] == 1:
    score += 4
if gears[3][0] == 1:
    score += 8

print(score)