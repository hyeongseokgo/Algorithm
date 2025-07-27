def solution(s):
    s = s.split(' ')
    s = list(map(int, s))
    
    return f'{min(s)} {max(s)}'