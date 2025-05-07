import sys
input = sys.stdin.readline

time = int(input())
num = list(map(int, input().split()))
num.sort()

cnt = 0

for i in range(time):
    N = num[i]
    sta = 0
    end = time-1
    while sta < end:
        if sta == i:
            sta += 1
            continue
        if end == i:
            end -= 1
            continue
        if num[sta] + num[end] == N:
            cnt += 1
            break
        elif num[sta] + num[end] < N:
            sta += 1
        else:
            end -= 1

print(cnt)