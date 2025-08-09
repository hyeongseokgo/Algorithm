N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

T_sum = 0
for i in range(len(size)):
    T_sum += ((size[i]-1)//T)+1
print(T_sum)
print(N//P, N%P)