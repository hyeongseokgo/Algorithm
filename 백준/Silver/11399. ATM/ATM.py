time = int(input())
num = sorted(list(map(int, input().split())))

result = 0
for i in range(time):
    result += num[i]*time
    time -= 1

print(result)