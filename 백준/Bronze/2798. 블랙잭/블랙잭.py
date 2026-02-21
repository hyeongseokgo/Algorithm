#블랙잭
from itertools import combinations

_, max_num = map(int, input().split())

num = list(map(int, input().split()))

result = list(combinations(num, 3))

temp = 0
for i in range(len(result)):
    a = sum(result[i])
    if a < max_num and a > temp:
        temp = a
    elif a == max_num:
        temp = a
        break
    else:
        continue



print(temp)