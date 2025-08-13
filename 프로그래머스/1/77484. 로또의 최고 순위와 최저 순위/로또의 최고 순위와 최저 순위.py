def solution(lottos, win_nums):
    answer = []
    
    yes = 0
    
    for i in lottos:
        if i in win_nums:
            yes += 1
    zero = lottos.count(0)
    
    
    return [min(7-(yes+zero), 6), min(7-yes,6)]