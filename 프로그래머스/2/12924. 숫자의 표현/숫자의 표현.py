def solution(n):
    num = [x for x in range(n)]
    s_num = []
    temp = 0
    count = 0
    for i in range(1,1+n):
        temp += i
        s_num.append(temp)
        
#     내가 사용한 방식은 누적합을 이용해서 푸는 방식이였는데 시간초과
    # for i in range(n):
    #     if s_num[i] < n:
    #         continue
    #     elif s_num[i] == n:
    #         count += 1
    #     else:
    #         for j in range(i):
    #             if s_num[i] - s_num[j] == n:
    #                 count += 1
    for i in range(n):
        if s_num[i] == n:
            count += 1
    
    start =0
    end = 1
    while end < n:
        if s_num[end]-s_num[start] == n:
            count += 1
            start += 1
            end += 1
        elif s_num[end]-s_num[start] > n:
            start += 1
        else:
            end += 1
    
    
    return count