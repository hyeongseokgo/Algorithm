time = int(input())

num = list(map(int, input().split()))

big = max(num)
isprime = [True]*(big+1)
isprime[0], isprime[1] = False, False

for i in range(2, int(big**0.5)+1):
    if isprime[i]:
        for j in range(i*i, big+1, i):
            isprime[j] = False

count = 0
for i in num:
    if isprime[i]:
        count+=1
print(count)