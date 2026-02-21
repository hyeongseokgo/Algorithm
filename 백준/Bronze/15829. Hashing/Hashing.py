time = int(input())

num = list(input())

result = 0
for i in range(len(num)):
    n = ord(num[i])-ord('a')+1
    result += n*(31**i)%1234567891

print(result)