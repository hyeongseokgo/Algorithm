from collections import deque

def solution(cacheSize, cities):
    cache = deque([])
    
    time = 0
    for i in cities:
        i = i.lower()
        
        if cache.count(i) == 0:
            cache.append(i)
            time += 5
            if len(cache) > cacheSize:
                cache.popleft()
        else:
            time += 1
            cache.remove(i)
            cache.append(i)
    
    return time