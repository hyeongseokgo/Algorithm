def solution(card):
    ran = list(range(1, len(card)+1))
    cnt = 0
    result = []
    zero = 0
    r = 0
    while len(ran) != 0:
        first = card[ran[0]-1]
        a = first
        for i in range(len(card)):
            b = card[a-1]

            ran.remove(a)
            cnt += 1
            a = b
            if first == b:
                break
        result.append(cnt)
        cnt = 0

    if len(result)== 1:
        r = 0
    else:
        result.sort(reverse=True)
        r = result[0]*result[1]

    return r