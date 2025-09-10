# 문제 : 입국심사
# 처음 문제를 봤을 때 만약 이 문제의 유형을 모른다고 생각했을때를 가정하고 풀었다.
# 근데 그냥 구현으로 풀기에는 심사관, 기다리는 사람이 너무 많아서 시간복잡도에 무조건 걸릴 예정
# 이제 유형을 알고 풀 수 있는지 테스트. 이분탐색이라는 유형을 알아도 이게 왜? 이분탐색? 인지 몰랐음

# 제일 작은 수를 left, 최악의 수를 right로 두고 center를 구하고 해당 초를 봤을 떄
# 몇 명을 입국심사 할 수 있는지 체크하고 그 값이랑 n이랑 비교해서 앞뒤를 정하는 방식.
# n이랑 같다고 해도 그 초가 최소가 아닐 수 있으니 left와 right가 같을때까지 계속 돌려줌.


def solution(n, times):
    answer = 0
    
    left = min(times)
    right = max(times)*n
    
    while left <= right:
        center = (left+right)//2
        min_people = 0
        for i in times:
            min_people += center//i
            if min_people >= n:
                break

        if min_people >= n:
            answer = center
            right = center-1
        elif n > min_people:
            left = center+1
        
    
    return answer