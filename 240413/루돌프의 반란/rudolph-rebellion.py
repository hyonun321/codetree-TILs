import sys

#sys.stdin = open('루돌프의반란4.txt', 'r')

N, M, P, C, D = map(int, input().split())

santa = [0] * (P + 1)
can_go_santa = [0] * (P + 1)
santa_point = [0] * (P + 1)
roodolf_map = [[0 for _ in range(N)] for _ in range(N)]
santa_map = [[0 for _ in range(N)] for _ in range(N)]
rx, ry = map(int, input().split())
rx -= 1
ry -= 1
roodolf_map[rx][ry] = 1


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def cal_dist(x1, y1, x2, y2):
    return abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2


rdx = [-1, -1, 0, 1, 1, 1, 0, -1]
rdy = [0, 1, 1, 1, 0, -1, -1, -1]

def roodolf_move():
    global rx, ry
    # 가장가까운 산타 찾기
    min_dist = 100000
    mx, my = 100000, 100000
    mnum = -1
    for num in range(1, P + 1):
        sx, sy = santa[num]
        if sx == -100: continue
        san_dist = cal_dist(sx, sy, rx, ry)
        if (min_dist) > (san_dist):
            min_dist = san_dist
            mx, my = sx, sy
        elif min_dist == san_dist:
            if (mx, my) <= (sx, sy):
                min_dist = san_dist
                mx, my = sx, sy
                mnum = num
    # print(mnum,mx,my)
    # mnum으로 출동 1칸
    rnum = -1
    min_rx, min_ry = 10000, 10000
    for num1 in range(8):
        nx, ny = rx + rdx[num1], ry + rdy[num1]
        if in_range(nx, ny):
            now_dist = cal_dist(nx, ny, mx, my)
            if now_dist < min_dist:  # 더작다면 거기로
                min_rx, min_ry = nx, ny
                min_dist = now_dist
                rnum=num1

    # print(min_dist,min_rx,min_ry)
    roodolf_map[rx][ry] = 0
    rx, ry = min_rx, min_ry
    roodolf_map[rx][ry] = 1
    # 충돌 구현해야함

    if santa_map[rx][ry] != 0 :
        snum = santa_map[rx][ry]
        santa_map[rx][ry] = 0
        santa_point[snum] += C
        can_go_santa[snum] = rounds +2

        sx,sy = santa[snum]

        nx,ny = sx+C*rdx[rnum],sy+C*rdy[rnum]
        number = snum
        if in_range(nx,ny) :
            # 연쇄충돌 만들어야함
            while True:
                if is_okay_santa(nx,ny,number): break
                nx,ny,number = push(nx,ny,number,rnum)

        else :
            santa[snum] = -100,-100
            santa_map[rx][ry] = 0


    return
def is_okay_santa(x,y,number):

    if in_range(x,y) and santa_map[x][y] == 0 :
        santa_map[x][y] = number
        santa[number] = x,y
        return True

    elif in_range(x,y) and santa_map[x][y] != 0 : return False
    else : #주의
        santa[number] = -100,-100
        return True
    return False

def push(nx,ny,number,rnum):
#   기존값을 넣고 새로운거 뺀다.
    nnumber = santa_map[nx][ny]
    santa[number] = nx,ny
    santa_map[nx][ny] = number

    nnx,nny = nx+rdx[rnum],ny+rdy[rnum]
    if in_range(nnx,nny) :
        return nnx,nny,nnumber
    else :
        return nnx,nny,nnumber

def one_santa_move(num,rounds):
    sx,sy = santa[num]
    if sx == -100 : return
    if can_go_santa[num] > rounds: return # 기절해서 못움직임
    min_x,min_y = sx,sy
    now_dist = cal_dist(sx,sy,rx,ry)
    s_num= -1
    for num1 in range(0,8,2):
        nx,ny = sx+rdx[num1],sy+rdy[num1]
        if in_range(nx,ny) and santa_map[nx][ny] == 0 :
            after_dist = cal_dist(nx,ny,rx,ry)
            if after_dist < now_dist:
                now_dist = after_dist
                min_x,min_y = nx,ny
                s_num = num1

    santa[num] = min_x,min_y
    santa_map[sx][sy] = 0
    santa_map[min_x][min_y] = num
    sx,sy = min_x,min_y
    #루돌프가 있나 체크해야함
    if sx == rx and sy == ry : #같다면
        #충돌처리해야함
        santa_map[sx][sy] = 0
        santa_point[num] += D
        can_go_santa[num] = rounds +2
        num2 = (s_num+4)%8

        nnx,nny =  sx+D*rdx[num2],sy+D*rdy[num2]
        if in_range(nnx,nny):
            #이곳에 산타가 있나 체크해야한다.
            number = num
            while True:
                if is_okay_santa(nnx,nny,number): break
                nnx,nny,number = push(nnx,nny,number,num2)
            pass
        else : #밖에 나간다
            santa[num] = -100,-100
            santa_map[sx][sy] = 0
            return







    return


def santa_move(rounds):
    for num in range(1, P + 1):
        one_santa_move(num,rounds)
    return


def is_not_santa_alive():
    for num in range(1, P + 1):
        sx, sy = santa[num]
        if sx == -100: continue
        return False
    return True


def santa_point_up():
    for number in range(1,P+1):
        sx,sy = santa[number]
        if sx == -100 : continue
        santa_point[number] +=1
    return


for _ in range(P):
    sn, sr, sc = map(int, input().split())
    sr -= 1
    sc -= 1
    santa[sn] = (sr, sc)
    santa_map[sr][sc] = sn


def see_map(number):
    print(number)
    print('루돌')
    for k in roodolf_map:
        print(*k)
    print('santa')
    for k1 in santa_map:
        print(*k1)
    print()


for rounds in range(M):
    #print('라운드')
    #see_map(rounds)
    roodolf_move()
    #see_map(2)
    if is_not_santa_alive(): break
    santa_move(rounds)
    #see_map(3)
    if is_not_santa_alive(): break
    santa_point_up()
    #if rounds == 6 :
    #    print(can_go_santa)
    #    break

for k in range(1, P + 1):
    print(santa_point[k], end=' ')