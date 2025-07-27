def solution(s):
    
    time = 0
    zero = 0
    
    while s != '1':
        s_one = s.replace('0', '')
        zero += len(s) - len(s_one)
        
        length = len(s_one)
        s = ''
        while length != 0:
            s = str(length%2) + s
            length = length//2
        time += 1
    
    return [time, zero]