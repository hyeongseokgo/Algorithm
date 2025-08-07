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