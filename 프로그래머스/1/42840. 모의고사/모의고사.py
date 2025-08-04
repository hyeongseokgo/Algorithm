def solution(answers):
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    time = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == (i%5)+1:
            time[0] += 1
        if answers[i] == num2[i%len(num2)]:
            time[1] += 1
        if answers[i] == num3[i%len(num3)]:
            time[2] += 1
    
    answer = []
    print(time)
    for i in range(3):
        if max(time) == time[i]:
            answer.append(i+1)
    
    return answer