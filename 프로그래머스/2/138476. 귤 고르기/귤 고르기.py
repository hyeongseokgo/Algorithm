from collections import Counter

def solution(k, tangerine):
    
    fruit = Counter(tangerine)
    cf = sorted(fruit.values(), reverse=True)
    wei = 0
    answer = 0
    for i in range(len(cf)):
        wei += cf[i]
        answer += 1
        if wei >= k:
            break
    
    return answer