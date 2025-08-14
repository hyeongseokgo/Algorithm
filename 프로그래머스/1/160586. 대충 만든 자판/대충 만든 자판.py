def solution(keymap, targets):
    answer = []
    
    for i in targets:
        click = 0
        for j in i:
            xmin = 101
            for k in keymap:
                if j in k:
                    xmin = min(k.index(j)+1, xmin)
            if xmin == 101:
                click = -1
                break
            else:
                click += xmin
        answer.append(click)
    
    
    
    
    return answer