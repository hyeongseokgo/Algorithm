stair = int(input())

point = [0]
for i in range(stair):
    point.append(int(input()))

dp = [0] * (stair+1)


if stair >= 1 :
    dp[1] = point[1]
if stair >= 2 :
    dp[2] = point[1]+point[2]
if stair >= 3 :
    dp[3] = max(point[1]+point[3], point[2]+point[3])

for i in range(4, stair+1):
    dp[i] = max(dp[i-2]+point[i], dp[i-3]+point[i-1]+point[i])

print(dp[stair])