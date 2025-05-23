T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())

    m_num = list(map(int, input().split()))

    point = 0
    cnt = 0
    temp = 0



    while 1:
        first_point = point



        for i in range(point, point+K+1):
            if m_num.count(i) != 0:
                temp = i

        if temp == first_point:
            cnt = 0
            break

        else:
            point = temp
            cnt += 1
            if point + K >= N:
                break

    print(f"#{test_case} {cnt}")
