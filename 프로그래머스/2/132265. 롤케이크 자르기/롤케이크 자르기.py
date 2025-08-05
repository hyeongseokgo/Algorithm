from collections import Counter
def solution(topping):
    answer = 0
    
    left_c = Counter()
    left_t = 0
    right_c = Counter(topping)
    right_t = len(right_c)
    
    for i in topping:
        if left_c[i] == 0:
            left_t += 1
        left_c[i] += 1
        
        right_c[i] -= 1
        if right_c[i] == 0:
            right_t -= 1
        
        if left_t == right_t:
            answer += 1
    
    return answer