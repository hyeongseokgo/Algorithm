
num = int(input())
number = []
for i in range(num):
    number.append(int(input()))

for i in range(num-1):
    for j in range(num-i-1):
        if number[j] > number[j+1]:
            number[j], number[j+1] = number[j+1], number[j]

for i in number:
    print(i)