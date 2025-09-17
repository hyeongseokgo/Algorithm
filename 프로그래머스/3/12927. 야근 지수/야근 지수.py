import heapq

def solution(n, works):
    answer = 0
    
    works = [-i for i in works]
    heapq.heapify(works)
    
    for i in range(n):
        big = heapq.heappop(works)
        if big == 0:
            break
        heapq.heappush(works, big+1)
    
    works = [i**2 for i in works]
    
    return sum(works)