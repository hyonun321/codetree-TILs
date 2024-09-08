import sys
from collections import deque

R,C,K = map(int,input().split())
board = [ [0 for _ in range(C)] for _ in range(R+3)]
gdx=[-1,0,1,0]
gdy=[0,1,0,-1]
fairy_position= [(-1,-1) for _ in range(K+1)]
result = 0
LEFT,RIGHT,DOWN=0,1,2
g_start = [-1]
g_exit = [-1]
deb = 0
for idx_i in range(K):
    ci,di = map(int,input().split())
    g_start.append(ci-1)
    g_exit.append(di)
def print_b(idx):
    for k in board:
        print(*[f"{num:>3}" for num in k])
    print(idx,"진행함")

# 차례대로 골렘 추가
  # 이때 위치에 넣어질수 없으면 초기화
# 각 골렘 아래로 이동
  # 방향 변경시 골렘 출구 돌리기
  # 서쪽 먼저 탐색 while각
# 가장 남쪽으로 이동

def init_board():
    global board
    board = [ [0 for _ in range(C)] for _ in range(R+3)]


def bfs(x,y):
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    queue = deque()
    visited = [[False for _ in range(C)]for _ in range(R+3)]
    visited[x][y] = True
    queue.append((x,y,abs(board[x][y])))
    max_x = x
    while queue:
        rx,ry,r_idx = queue.popleft()
        for d in range(4):
            nx,ny = rx+dx[d],ry+dy[d]
            if (in_range(nx,ny)  and abs(board[nx][ny]) == r_idx and visited[nx][ny] == False ):
                queue.append((nx,ny,abs(board[nx][ny])))
                visited[nx][ny] = True
                max_x = max(max_x,nx)
            elif  (in_range(nx,ny) and board[rx][ry] <0 and abs(board[nx][ny]) != r_idx and board[nx][ny] != 0  and visited[nx][ny] == False) :
                new_fairy_idx = board[nx][ny]
                queue.append((nx, ny,abs(board[nx][ny])))
                visited[nx][ny] = True
                max_x = max(max_x, nx)
    return max_x

def one_gol_down(idx):
    g_col = g_start[idx]
    for row in range(R+2,0,-1):
        if(check_gol_body(row,g_col)):
            if(move_left_right(row,g_col,idx)):
                return True
            return False
    return False

def move(x,y,idx) :
    if (idx == LEFT):
        return (x,y)
    elif (idx == RIGHT):
        return (x,y)
    return (-1,-1)

def move_left_right(x,y,g_number):
    # 여기가 어려운 각
    while(1):
        if (check_gol_position(x,y,DOWN)):
            x = x + 1
        else :
            if (check_gol_position(x,y,LEFT)):
                g_exit[g_number] = (g_exit[g_number] - 1 )%4
                #print("왼쪽 자리있음",g_number)
                x = x + 1
                y = y - 1
            else :
                if(check_gol_position(x,y,RIGHT)):
                    g_exit[g_number] = (g_exit[g_number] + 1) % 4
                    #print("오른쪽 자리 있음",g_number)
                    x = x + 1
                    y = y + 1

                else : # 제자리
                    #print("제자리", g_number)
                    # 내려갈수있나 봐야함.

                    if not (check_gol_body(x,y)):
                        return False
                    break
    fairy_position[g_number] = (x, y)
    board_draw_by_fairy(g_number)
    for item in range(C):
        if board[0][item] != 0 :
            return False
        if board[1][item] != 0 :
            return False
        if board[2][item] != 0 :
            return False
    #print_b()
    return True
    # 그냥 그자리 그대로

def board_draw_by_fairy(g_number):
    x,y = fairy_position[g_number]
    for d in range(4):
        nx,ny = x+gdx[d],y+gdy[d]
        if (in_range(nx,ny) and board[nx][ny] == 0) :
            board[nx][ny] = g_number
    if in_range(x,y) and board[x][y] == 0:
        board[x][y] = g_number
    nx = x +gdx[g_exit[g_number]]
    ny = y +gdy[g_exit[g_number]]
    board[nx][ny] = -g_number
def check_gol_position(x,y,position):
    if ( position == LEFT):
        if(in_range(x,y-2) and board[x][y-2] == 0) and (in_range(x-1,y-1) and board[x-1][y-1]== 0) and (in_range(x+1,y-1) and board[x+1][y-1]== 0) and ((in_range(x + 1, y - 2) and board[x + 1][y - 2] == 0 )) and ((in_range(x + 2, y - 1) and board[x + 2][y - 1] == 0 ) ):
            return True
        return False

    elif ( position == RIGHT):
        if (in_range(x, y + 2) and board[x][y + 2] == 0) and (in_range(x + 1, y + 1) and board[x + 1][y + 1]== 0) and ((in_range(x - 1, y + 1) and board[x - 1][y + 1] == 0 ))and ((in_range(x + 2, y + 1) and board[x + 2][y + 1] == 0 )) and ((in_range(x + 1, y + 2) and board[x + 1][y + 2] == 0 )):
            return True
        return False
    elif (position == DOWN):
        if (in_range(x+2,y) and board[x+2][y] == 0 ) and (in_range(x+1,y-1) and board[x+1][y-1] == 0 ) and (in_range(x+1,y+1) and board[x+1][y+1] == 0 ) :
            return True
        return False

def fairy_move_and_point_up(idx):
    global result
    x,y = fairy_position[idx]
    x = x+gdx[g_exit[idx]]
    y = y+gdy[g_exit[idx]]
    bx = bfs(x,y)
    result += (bx-2) # 인덱스 보정
    if deb:
        print(idx,"의",bx-2,"만큼더해서",result)
    return

def in_range(x,y):
    return 0<=x<R+3 and 0<=y<C

def check_gol_body(x,y):
    ## 가장 맨위일때도 잘라버려야함.
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    for d in range(4):
        nx,ny = x+dx[d],y+dy[d]
        if not (in_range(nx,ny) and board[nx][ny] == 0) :
            return False
    if not in_range(x,y) and board[x][y] == 0:
        return False
    return True

for gol_idx in range(1,K+1):

    gol_ok = one_gol_down(gol_idx)
    if not (gol_ok):
        init_board()
        if deb:
            print_b(gol_idx)
        continue
    fairy_move_and_point_up(gol_idx)
    if deb:
        print_b(gol_idx)
print(result)