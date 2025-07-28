def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            answer = answer + ' '
        elif s[i] >= 'a' and s[i] <= 'z':
            if ord(s[i])+n > ord('z'):
                temp = ord('a') + (ord(s[i])+n)%(ord('z')+1)
                answer = answer + chr(temp)
            else:
                answer = answer + chr(ord(s[i])+n)
        else:
            if ord(s[i])+n > ord('Z'):
                temp = ord('A') + (ord(s[i])+n)%(ord('Z')+1)
                answer = answer + chr(temp)
            else:
                answer = answer + chr(ord(s[i])+n)
    return answer