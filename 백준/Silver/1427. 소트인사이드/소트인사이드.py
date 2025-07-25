lis = list(input())
ans = []
for i in range(len(lis)):
    a = lis.index(max(lis))
    ans.append(lis[a])
    lis.pop(a)
    
print(int(''.join(ans)))
