def solution(n):
#     당연히 피보나치라길래 재귀썼는데 이건 절대 재귀 안된다.
#     save = [-1] *(n+1)
#     def piv(num):
        
#         if num <=1 :
#             return num
#         elif save[num] != -1:
#             return save[num]
#         else:
#             save[num] =  piv(num-1) + piv(num-2)    
#         return save[num]

    piv = [0, 1]+[-1]*n
    for i in range(2, n+1):
        piv[i] = (piv[i-1]+piv[i-2])%1234567
    
    return piv[n]