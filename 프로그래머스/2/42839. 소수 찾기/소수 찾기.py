# 소수 찾기 문제
# 1. 나온 numbers의 모든 경우의 수를 구하기 -> 순열로 dfs 조지기
#     -> 파이썬의 라이브러리 itertools.permutations를 쓰면 쉽지만 연습겸 dfs

# 2. 모든 순열을 set()에 넣어서 중복 없애기

# 3. 이걸 하나씩 소수인지 판별하는데 하나씩 for문으로 돌리면
#    O(총 set개수 * 한 값의 제곱근) -> 문자열 길어지면 무우우우조건 시간초과
#    이럴때 쓰는게 바아로 에라토스테네스 체 -> 간단하게 말하면 소수의 곱들은 소수가 아님
#    이걸 쓰면 O(log m) 정도로 소수를 구할 수 있고 카운트는 O(1)로 매우 빠름

def solution(numbers):
    all_num = list(numbers)
    all_per = set()
    
    
    # DFS 순열 만들기
    def dfs(num, check):
        if len(num) >= 1:
            all_per.add(int(''.join(num)))
            
        for i in range(len(all_num)):
            if check[i] == False:
                check[i] = True
                num.append(all_num[i])
                dfs(num, check)
                num.pop()
                check[i] = False
    dfs([], [False]*len(all_num))
    
    # 에라토스테네스의 체 발동
    big = max(all_per)
    is_prime = [True]*(big+1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(big**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, big+1, i):
                is_prime[j] = False
    
    # 소수 카운트
    count = 0
    for i in all_per:
        if is_prime[i] == True:
            count += 1
    
            
        
    
    return count