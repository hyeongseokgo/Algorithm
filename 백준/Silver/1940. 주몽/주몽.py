# # 백준용 : sys.stdin.readline
import sys
input = sys.stdin.readline

time = int(input())
corr = int(input())
num = list(map(int, input().split()))
num.sort()

start_p = 0
end_p = time-1

cnt = 0

while start_p < end_p:
    if num[start_p] + num[end_p] == corr:
        start_p += 1
        end_p -= 1
        cnt += 1
    elif num[start_p] + num[end_p] > corr:
        end_p -= 1
        start_p = 0
    else:
        start_p += 1
print(cnt)