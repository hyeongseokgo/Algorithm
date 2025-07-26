def solution(arr):
    arrmin = min(arr)
    answer = []
    for i in range(len(arr)):
        if arr[i] != arrmin:
            answer.append(arr[i])
    if len(answer) == 0:
        answer.append(-1)
    return answer