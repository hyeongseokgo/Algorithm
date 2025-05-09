 # 백준용 : sys.stdin.readline
import sys
input = sys.stdin.readline

num_l = int(input())
num_s = []

for i in range(num_l):
    num_s.append(int(input()))

stack = [0]
point = 0

ans = []


for i in range(num_l):
    if stack[len(stack)-1] < num_s[i]:
        for k in range(num_s[i]- point):
            point+= 1
            stack.append(point)
            ans.append('+')
        stack.pop()
        ans.append('-')
    elif stack[len(stack)-1] == num_s[i]:
        stack.pop()
        ans.append('-')
    else:
        ans.append(0)
        print('NO')
        break

if ans[len(ans)-1] != 0:
    for i in range(len(ans)):
        print(ans[i])
