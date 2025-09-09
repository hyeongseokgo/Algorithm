def solution(n, times):
    answer = 0
    
    left = min(times)
    right = max(times)*n
    
    while left <= right:
        center = (left+right)//2
        min_people = 0
        for i in times:
            min_people += center//i
            if min_people >= n:
                break

        if min_people >= n:
            answer = center
            right = center-1
        elif n > min_people:
            left = center+1
        
    
    return answer