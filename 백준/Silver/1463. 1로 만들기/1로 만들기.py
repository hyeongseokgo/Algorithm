# 그리디로 당연히 안 풀릴줄 알았음,,
# 유명한 dp문제라고 하네,, 밑에는 억지로 그리디로 푼 흔적
# num = int(input())

# time = 0

# while num != 1:


#     if num % 3 == 1:
#         num -= 1
#     elif num % 3 == 0:
#         num = num // 3
#     elif num % 2 == 0:
#         num = num // 2
#     else:
#         num -= 1
#     time += 1

# print(time)

num = int(input())

dp = [0]*(num+1)

for i in range(2, num+1):
    dp[i] = dp[i-1]+1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
print(dp[num])