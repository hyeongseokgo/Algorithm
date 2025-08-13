def solution(sizes):
    top = 0
    bot = 0
    
    for a, b in sizes:
        if top <= max(a, b):
            top = max(a, b)
        if bot <= min(a, b):
            bot = min(a, b)
    
    
    
    
    answer = top * bot
    return answer