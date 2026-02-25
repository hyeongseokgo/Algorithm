# 시간초과
# why? temp in pocket, index 부분에서 O(N)
# 연속 두번 써버림.

# mon, qna = map(int, input().split())

# pocket = []
# for i in range(mon):
#     pocket.append(input())

# for i in range(qna):
#     temp = input()
#     if temp in pocket:
#         print(pocket.index(temp)+1)
#     else:
#         print(pocket[int(temp)-1])


# 따라서 물어본 결과 딕셔너리를 이용.
# 두개로 하면 더 편함.
mon, qna = map(int, input().split())

name_to_num = {}
num_to_name = {}

for i in range(1, mon + 1):
    name = input()
    name_to_num[name] = i
    num_to_name[i] = name

for _ in range(qna):
    temp = input()

    if temp.isdigit():
        print(num_to_name[int(temp)])
    else: 
        print(name_to_num[temp])