from collections import Counter
def solution(want, number, discount):
    answer =0
    wn = {}
    fail = False
    for i in range(len(number)):
        wn[want[i]] = number[i]
    wn = Counter(wn)
    
    for i in range(len(discount)-10+1):
        temp = Counter(discount[i:i+10])
        if len(wn-temp) == 0:
            answer += 1
    
    
    return answer