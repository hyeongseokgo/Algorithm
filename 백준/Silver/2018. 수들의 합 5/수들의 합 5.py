start_p = 1
end_p = 1
cnt = 1
sum = 1

num = int(input())

while num != end_p:
    if sum == num:
        end_p += 1
        sum += end_p
        cnt += 1
    elif sum > num:
        sum -= start_p
        start_p += 1
    else:
        end_p += 1
        sum += end_p
        
print(cnt)