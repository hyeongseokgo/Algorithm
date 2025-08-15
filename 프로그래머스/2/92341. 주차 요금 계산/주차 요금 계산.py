def solution(fees, records):
    answer = []
    
    time = []
    number = []
    mini = []
    
    for i in records:
        a = i.split()
        temp = int(a[0][:2])*60 + int(a[0][3:])
        if a[2] == 'IN':
            if a[1] in number:
                time[number.index(a[1])] = temp
            else:
                number.append(a[1])
                time.append(temp)
                mini.append(0)
        else:
            mini[number.index(a[1])] += temp- time[number.index(a[1])]
            time[number.index(a[1])] = -1
        
    for i in range(len(time)):
        if time[i] != -1:
            mini[i] += 23*60+59-time[i]
    
    num_sort = sorted(number)
    answer = [0] *len(number)
    
    for i in range(len(mini)):
        index = num_sort.index(number[i])
        if mini[i] <= fees[0]:
            answer[index] = fees[1]
        else:
            answer[index] = fees[1] + ((mini[i]-fees[0]-1)//fees[2] +1)*fees[3]
    
    
    
    return answer