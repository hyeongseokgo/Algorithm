import collections

def solution(s):
    a = s.replace('{', '')
    a = a.replace('}', '')
    a = a.split(',')
    counts = collections.Counter(a)
    d1 = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    abc = []
    for i in d1:
        abc.append(int(i[0]))
    return abc