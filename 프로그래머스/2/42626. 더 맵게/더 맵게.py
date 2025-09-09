# 더 맵게 / 우선순위 힙 문제
# 처음 문제를 봤을 때 단순히 정렬하고 하면 쉽겠다 라고 생각하고 다음과 같은 코드를 짰는데
# 스코빌의 길이가 백만까지 있기에 시간초과가 당연히 났다.
# 그때 우선순위 큐를 따로 공부해서 직접 써보니 잘 돌아갔다.
# 그래서 왜 잘된거? 우선순위 큐의 작동 원리가 뭔데??

# 우선순위 큐는 일반적으로 작은 순서부터 정렬되어 있는 큐로 알고 있었는데
# 이는 완전 이진트리 구조로 제일 작은 값부터 꼭대기를 차지함.


# def solution(scoville, K):
#     scoville.sort()
#     answer = 0
    
#     while scoville[0] <= K:
#         if len(scoville) <= 1:
#             return -1
#         scoville[0] = scoville[0] + scoville[1]*2
#         del scoville[1]
#         scoville.sort()
#         answer += 1
    
    
#     return answer

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville) * 2
        heapq.heappush(scoville, a+b)
        answer += 1
    
    return answer