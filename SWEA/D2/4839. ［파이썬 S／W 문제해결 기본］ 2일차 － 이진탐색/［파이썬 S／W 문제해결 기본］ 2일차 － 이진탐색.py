T = int(input())

def find_page(page_w, page_f):
    l1 = 1
    r1 = page_w
    cnt = 0
    while 1:
        c = int((l1+r1)/2)
        cnt += 1
        if c == page_f:
            break
        elif c < page_f:
            l1 = c
        else:
            r1 = c
    return cnt

for test_case in range(1, T + 1):
    page_w , page_a, page_b = map(int, input().split())
    if find_page(page_w, page_a) > find_page(page_w, page_b):
        print(f'#{test_case} B')
    elif find_page(page_w, page_a) < find_page(page_w, page_b):
        print(f'#{test_case} A')
    else:
        print(f'#{test_case} 0')

