def solution(arr):
#      내가 푼 방식
#       1. 첫수는 answer에 넣기  2. arr값을 하나씩 체크하면서 answer top과 겹치면 패스 아니면 append
    answer = []
    answer.append(arr.pop(0))
    arr_o = arr.copy()
    for i in arr_o:
        if answer[-1] == i:
            pass
        else:
            answer.append(i)
            
    return answer