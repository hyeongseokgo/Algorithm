# 목표 : 로봇청소기가 청소한 칸의 개수 구하기
# 단순 시뮬
# 입력 : n, m 전체 칸의 수 , 바라보고 있는 방향 0~3 위부터 시계방향
# 출력 : 청소기가 다 돌아간 상태의 총 청소칸

# 변수 : 방향, 청소 유무 리스트, 전체 방 리스트, 로봇위치

direct = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 0, 1, 2, 3

n, m = map(int, input().split())
r_y, r_x, r_d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(n)]
check = [[0]*m for _ in range(n)]

# 루프 : 청소기 칸 청소(현재 칸 1로 만들기)
#        주변 장애물 확인 (동서남북 확인해서 1인지 확인)
#        클린 칸 확인 (동서남북 확인해서 1인지 확인)
#        if 필요한 청소칸 있나 없나?
#        없으면 방향 유지한채로 +2%4 해서 후진만 하기 - 이동불가면 break
#        있으면 -1%4 방향 회전하고 방향앞에 청소칸이 0이면 한칸 전진 아니면 continue


def clean_check(x, y, d): #로봇의 x,y, 방향
  for dx, dy in direct:
    nx = dx+x
    ny = dy+y
    if 0 <= nx < m and 0 <= ny < n and not room[ny][nx] and not check[ny][nx]:
      return 1
  return 0

while 1:
  check[r_y][r_x] = 1
  
  # [print(x) for x in check]
  # print()

  if clean_check(r_x, r_y, r_d): #청소가능한 칸 발견
    
    r_d = (r_d - 1)%4

    nx = direct[r_d][1]+r_x
    ny = direct[r_d][0]+r_y

    if 0<=nx <m and 0<=ny< n and not room[ny][nx] and not check[ny][nx]:
      r_x = direct[r_d][1]+r_x
      r_y = direct[r_d][0]+r_y

  else:
    nd = (r_d +2)%4
    nx = direct[nd][1]+r_x
    ny = direct[nd][0]+r_y

    if 0<=nx <m and 0<=ny< n and not room[ny][nx]:
      r_x = direct[nd][1]+r_x
      r_y = direct[nd][0]+r_y
    else:
      break
  
print(sum( sum(x) for x in check ))




