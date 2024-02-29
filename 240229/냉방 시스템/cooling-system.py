import sys
from collections import deque
sys.stdin = open('냉방 시스템.txt','r')
deb = 1
#input
n,m,k = map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(n)]
block = [ [ [False]*4 for _ in range(n)] for _ in range(n)]
cool_map = [ [0 for _ in range(n)] for _ in range(n)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]
dxs=[-1,0,1,0]
dys=[0,-1,0,1]

#2시간33분 스탑
# 바람 퍼지는 부분에서 멈추기


#에어컨 : 2 왼쪽, 3 위쪽, 4오른쪽, 5 아래
def in_range(x,y) :
    return 0<=x<n and 0<=y<n
for _ in range(m) :
    x,y,s = map(int,input().split())
    x-=1
    y-=1
    block[x][y][s] = True # 수정함
    nx,ny = x+dxs[s],y+dys[s]
    if in_range(nx,ny) :
        block[nx][ny][3-s] = True

visited = [
    [False] * n
    for _ in range(n)
]
def clear_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def aircondition():
    dict_dir = {
        2:3,
        3:0,
        4:1,
        5:2
    }
    for i in range(n) :
        for j in range(n) :
            if 1< maps[i][j] < 6:
                #cool_temp_map = wind_up(i,j,maps[i][j])
                dirr = dict_dir[maps[i][j]]
                nx,ny = i+dx[dirr],j+dy[dirr]
                clear_visited()
                spread(nx,ny,dirr,5)
    return

def rev_dir(x_diff, y_diff):
    for i, (dx, dy) in enumerate(zip(dxs, dys)):
        if dx == x_diff and dy == y_diff:
            return i

    return -1

def spread(x,y,move_dir,power):#재귀함수써야하네..  2시간30분에 포기.
    if power == 0:
        return

    # 방문 체크를 하고, 해당 위치에 power를 더해줍니다.
    visited[x][y] = True
    cool_map[x][y] += power

    # Case 1. 직진하여 전파되는 경우입니다.
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    if in_range(nx, ny) and not visited[nx][ny] and not block[x][y][move_dir]:
        spread(nx, ny, move_dir, power - 1)

    # Case 2. 대각선 방향으로 전파되는 경우입니다.
    if dxs[move_dir] == 0:
        for nx in [x + 1, x - 1]:
            ny = y + dys[move_dir]
            # 꺾여 들어가는 곳에 전부 벽이 없는 경우에만 전파가 가능합니다.
            if in_range(nx, ny) and not visited[nx][ny] and \
                    not block[x][y][rev_dir(nx - x, 0)] and not block[nx][y][move_dir]:
                spread(nx, ny, move_dir, power - 1)

    else:
        for ny in [y + 1, y - 1]:
            nx = x + dxs[move_dir]
            # 꺾여 들어가는 곳에 전부 벽이 없는 경우에만 전파가 가능합니다.
            if in_range(nx, ny) and not visited[nx][ny] and \
                    not block[x][y][rev_dir(0, ny - y)] and not block[x][ny][move_dir]:
                spread(nx, ny, move_dir, power - 1)
    # if power == 0 :
    #     return
    # visited[a][b] = True
    # cool_map[a][b] += power
    #
    # # 직진전파
    #
    # nx,ny = x+dxs[direction],y+dys[direction]
    # if in_range(nx,ny) and not visited[nx][ny] and not wall[x][y][direction]:
    #     wind_blow_up(nx,ny,direction,power-1)
    # if dys[direction] == 0 : #오른족으로 간다하면, dxs 1, -1 일때니까
    #     for ny in [y+1 , y-1] :
    #         nx = x+dxs[direction]
    #         if in_range(nx,ny) and not visited[nx][ny] and not wall[x][y][rev_dir(0,ny-y)] and not wall[x][ny][direction] :
    #
    # # 대각전파

    return

def mix_cool_air():
    #이제 벽반영을 해야함.  -[x]

    temp_cool = [ [0 for _ in range(n)] for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            if cool_map[i][j] > 0 :
                a = cool_map[i][j]
                for num in range(4) :
                    nx,ny = i+dx[num],j+dy[num]
                    if in_range(nx,ny) :
                        #여기서 벽 조건넣어야함.
                        if block[nx][ny][0] == True or block[i][j][0] == True  :#위에 있을때
                            if num == 0 or num == 2 : continue
                        if block[nx][ny][1] == True or block[i][j][1] == True:
                            if num == 1 or num == 3 : continue

                        b = cool_map[nx][ny]
                        diff = abs(a-b)
                        if diff >= 4 :
                            mok = diff//4
                            if a>b :
                                temp_cool[i][j] -= mok
                                temp_cool[nx][ny] += mok
                            else :
                                temp_cool[nx][ny] -=mok
                                temp_cool[i][j] += mok
    for i in range(n) :
        for j in range(n) :
            cool_map[i][j] += temp_cool[i][j]//2
    if deb:
        print('시원함퍼지기')
        for k in cool_map:
            print(*k)
        print()


    return
def cool_down():
    inputs = [0,n-1]
    for io in inputs:
        for i in range(0,n-1) :
            if cool_map[io][i] >0:
                cool_map[io][i] -=1
        for i in range(1,n-1) :
            if cool_map[i][io] >0:
                cool_map[i][io] -=1

    cool_map[0][n-1] -=1
    cool_map[n-1][n-1] -=1
    if cool_map[0][n-1] < 0 :
        cool_map[0][n - 1] =0
    if cool_map[n-1][n-1] < 0 :
        cool_map[n-1][n - 1] =0
    if deb:
        print('주변자리 차가워짐')
        for k in cool_map:
            print(*k)
        print()
    return

def chk_samoosil():
    count = 0
    cool_count = 0
    for i in range(n) :
        for j in range(n) :
            if maps[i][j] == 1 :
                count += 1
                if cool_map[i][j] >= k :
                   cool_count +=1
    if count == cool_count :
        return True
    else :
        return False


possible = False
for rounds in range(1,8):
    if deb:
        for ttt2 in maps:
            print(*ttt2)
    aircondition()
    mix_cool_air()
    cool_down()
    if chk_samoosil() :
        print(rounds)
        possible = True
        break
if not possible :
    print(-1)