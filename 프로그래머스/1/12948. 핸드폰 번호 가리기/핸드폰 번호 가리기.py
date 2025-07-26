def solution(phone_number):
    phone = '*'*(len(phone_number)-4)
    phone += phone_number[-4:]
    return phone