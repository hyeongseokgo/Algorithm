insert = int(input())
score = list(map(int, input().split()))
sum = 0
top = max(score)

for i in score:
    sum += i / top * 100

print(sum/insert)