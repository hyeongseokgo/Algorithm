def trans(num, n):
    string = ''
    ten = ['A', 'B', 'C','D','E', 'F']
    a = ''
    while n <= num:
        if num%n >= 10:
            a = ten[(num%n)-10]
        else:
            a = str(num%n)
        
        string = a + string
        num = num//n
        
    if num >= 10:
        a = ten[(num)-10]
    else:
        a = str(num)
    string = a + string
    return string

def solution(n, t, m, p):
    answer = ''
    all_t = ''
    
    for i in range(t*m):
        all_t = all_t + trans(i, n)
        if len(all_t) > t*m:
            break
    
    return all_t[p-1:t*m:m]