def solution(book_time):
    time = []
    room = []
    for s, e in book_time:
        start = int(s[:2])*60 + int(s[3:])
        end = int(e[:2])*60 + int(e[3:]) + 10
        time.append((start, end))
    
    time.sort()
    
    for start, end in time:
        check = False
        for i in range(len(room)):
            if room[i] <= start:
                room[i] = end
                check = True
                break
        if check == False:
            room.append(end)
    
    
    return len(room)