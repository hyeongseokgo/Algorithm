def solution(number):
    answer =0
    for bit in range(1<<len(number)):
        if bin(bit).count('1') == 3:
            sel = []
            for i in range(len(number)):
                if bit & (1<<i):
                    sel.append(number[i])
            if sum(sel) == 0:
                answer += 1
    
    return answer