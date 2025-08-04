def solution(phone_book):
    
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        a = len(phone_book[i])
        if phone_book[i+1][:a] == phone_book[i]:
            return False
    
    
    return True