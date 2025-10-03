N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

pattern_w = ["WBWBWBWB", "BWBWBWBW"] * 4  # 왼쪽 위가 W
pattern_b = ["BWBWBWBW", "WBWBWBWB"] * 4  # 왼쪽 위가 B

ans = 64  # 최악의 경우 (8*8 전부 칠하기)

# 슬라이딩 윈도우로 8x8 잘라서 검사
for x in range(N-7):
    for y in range(M-7):
        cnt_w = 0
        cnt_b = 0
        for i in range(8):
            for j in range(8):
                if board[x+i][y+j] != pattern_w[i][j]:
                    cnt_w += 1
                if board[x+i][y+j] != pattern_b[i][j]:
                    cnt_b += 1
        ans = min(ans, cnt_w, cnt_b)

print(ans)
