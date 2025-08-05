import copy
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    gyo = 0
    
    string1 = [str1[i:i+2] for i in range(len(str1)-1)]
    string2 = [str2[i:i+2] for i in range(len(str2)-1)]
    new1 = []
    new2 = []
    
    
    for i in range(len(string1)):
        if string1[i].isalpha():
            new1.append(string1[i])
    for i in range(len(string2)):
        if string2[i].isalpha():
            new2.append(string2[i])
    string1 = new1.copy()
    string2 = new2.copy()
    
    for i in range(len(string1)):
        if string1[i] in new2:
            new2.remove(string1[i])
            gyo +=1
    hap = len(string1) + len(string2) - gyo
    
    if hap == 0:
        return 65536
    else:
        return int(gyo/hap *65536)
