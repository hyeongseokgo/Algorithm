import sys
input = sys.stdin.readline

data , q = map(int, input().split())
mylist = list(map(int, input().split()))

##구간합 구하기
for i in range(1, data):
    mylist[i] += mylist[i-1]

for j in range(int(q)):
    a, b = map(int, input().split())
    if a == 1:
        print(mylist[b-1])
    else:
        print(mylist[b-1]-mylist[a-2])
