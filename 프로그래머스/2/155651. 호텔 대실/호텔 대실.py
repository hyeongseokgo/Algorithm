# 호텔 대실 문제
# 처음 이 문제를 봤을 때 방 배정 문제는 보통 그리디 문제로 생각했기에 그리디로 생각함.
# 1. 일단 예약 시간들을 모두 정수형으로 풀면 계산하기 편하기에 시간나오는 문제는 다 정수형으로 풀기
# 2. 이 예약시간들을 시작순서대로 정렬해주고 예약시간 하나씩 보면서 넣을 예정
# 3. 방 리스트 안에는 종료점을 넣어서 내가 예약하는 시작점이랑 비교해서 시작점이 더 크다면 배정.
#    만약 종료점이 더 크면 그 방 못씀
# 4. 방 다 확인했는데 다 예약 못하면 방 추가

def solution(book_time):
    time = []
    room = []
    
    # 예약 시간 정수형으로 돌리기
    for s, e in book_time:
        start = int(s[:2])*60 + int(s[3:])
        end = int(e[:2])*60 + int(e[3:]) + 10
        time.append((start, end))
    
    # 정렬
    time.sort()
    
    # 예약시간 하나씩 보면서 방 체크
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