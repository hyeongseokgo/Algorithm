def solution(n):
    answer = []
    def hanoi(n, A, B, C):
        if n == 1:
            answer.append([A, B])
            return
        hanoi(n-1, A, C, B)
        answer.append([A, B])
        hanoi(n-1, C, B, A)
    hanoi(n, 1, 3, 2)
    return answer