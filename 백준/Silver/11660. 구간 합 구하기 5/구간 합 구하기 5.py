import sys
input = sys.stdin.readline

n, cnt = map(int, input().split())
n += 1
arr = [[0 for j in range(n)] for i in range(n)]

for i in range(1, n):
    arr[i] = [0] + list(map(int, input().split()))

for i in range(1, n):
    for j in range(1, n):
        arr[j][i] += arr[j][i-1] + arr[j-1][i] - arr[j-1][i-1]

for i in range(cnt):
    x1, y1, x2, y2 = map(int, input().split())
    print(arr[x2][y2]-arr[x2][y1-1]-arr[x1-1][y2]+arr[x1-1][y1-1])