def solution(name, yearning, photo):
    d_list = dict(zip(name, yearning))
    sh = len(photo)
    i = 0
    sum_photo = []

    while(i<sh):
        s = 0
        for j in range(len(photo[i])):
            if name.count(photo[i][j]) == 0:
                pass
            else:
                s += d_list[photo[i][j]]
        i+= 1
        sum_photo.append(s)      
    return sum_photo