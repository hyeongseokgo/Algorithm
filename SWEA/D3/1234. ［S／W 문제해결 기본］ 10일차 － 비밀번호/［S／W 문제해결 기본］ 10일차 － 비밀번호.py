T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num, password = map(str, input().split())

    stc = []

    num = int(num)

    for i in range(num):
        if len(stc) == 0:
            stc.append(password[i])

        else:
            if stc[len(stc)-1] == password[i]:
                stc.pop()
            else:
                stc.append(password[i])

    print(f"#{test_case} {int(''.join(stc))}")

