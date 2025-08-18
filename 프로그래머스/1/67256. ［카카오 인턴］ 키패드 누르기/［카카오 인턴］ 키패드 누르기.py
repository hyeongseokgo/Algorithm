def solution(numbers, hand):
    answer = ''
    
    lefttype = ['1', '4', '7']
    righttype = ['3', '6', '9']
    
    left = [3, 0]
    right = [3, 2]
    
    for i in numbers:
        if i == 0:
            i = 11
        
        
        if i %3 == 1:
            answer = answer + 'L'
            left = [(i-1)//3, (i-1)%3]
        elif i%3 == 0:
            answer += 'R'
            right = [(i-1)//3, (i-1)%3]
        else:
            l_dis = abs((i-1)//3 - left[0]) + abs((i-1)%3 - left[1])
            r_dis = abs((i-1)//3 - right[0]) + abs((i-1)%3 - right[1])
            if l_dis < r_dis:
                answer = answer + 'L'
                left = [(i-1)//3, (i-1)%3]
            elif l_dis > r_dis:
                answer += 'R'
                right = [(i-1)//3, (i-1)%3]
            else:
                if hand == 'right':
                    answer += 'R'
                    right = [(i-1)//3, (i-1)%3]
                else:
                    answer = answer + 'L'
                    left = [(i-1)//3, (i-1)%3]
    
    return answer