def solution(d, budget):
    d.sort()
    time =0
    b_sum =0
    for i in range(len(d)):
        b_sum += d[i]
        if b_sum > budget:
            break
        time += 1
    return time