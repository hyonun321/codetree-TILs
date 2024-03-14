import sys
#sys.stdin = open('루돌프의반란.txt','r')
n,m,p,c,d = map(int,input().split())
r_x,r_y = map(int,input().split())
r_x-=1
r_y-=1
r_d=-1
ROODOLF = 1 
SANTA = 0
santa_map= [ [ 0 for _ in range(n)] for _ in range(n)]
roodolf_map = [ [ 0 for _ in range(n)] for _ in range(n)]
roodolf_map[r_x][r_y] = 1
santa_point = [0 for _ in range(p+1)]
santa_appa = [0 for _ in range(p+1)]
santa_direction = [-1 for _ in range(p+1)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
for _ in range(p):
    t_num,tx,ty = map(int,input().split())
    tx-=1
    ty-=1
    santa_map[tx][ty] = t_num


def in_range(x,y):
    return 0<=x<n and 0<=y<n

def cal_distance(x1,y1,x2,y2):
    return (x1-x2)**2+(y1-y2)**2

def find_short_distance_santa(r_x,r_y):
    si,sj = 10000,10000
    s_distance = 10000
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1) : 
            if santa_map[i][j] > 0 : 
                distance = cal_distance(r_x,r_y,i,j)
                if distance < s_distance:
                    s_distance = distance
                    si,sj=i,j

    return si,sj

rdx=[-1,-1,0,1,1, 1, 0,-1]
rdy=[ 0, 1,1,1,0,-1,-1,-1]

def roodolf_move():
    global r_x,r_y,r_d,c
    san_x,san_y = find_short_distance_santa(r_x,r_y)
    x,y=r_x,r_y
    final_distance = 10000
    final_direction = -1
    for num in range(8):
        nx,ny = x+rdx[num],y+rdy[num]
        if in_range(nx,ny) :
            after_distance = cal_distance(san_x,san_y,nx,ny)
            if after_distance < final_distance:
                final_distance = after_distance
                final_direction = num
    r_d = final_direction
    roodolf_map[r_x][r_y] = 0 
    r_x,r_y = x+rdx[r_d],y+rdy[r_d]
    roodolf_map[r_x][r_y] = 1
    rx,ry = r_x,r_y
    # 산타 충돌체크 
    if santa_map[rx][ry] != 0 :
        temp_num = santa_map[rx][ry]
        santa_point[temp_num] += c
        while True : # 산타가있다면?
            rx,ry,temp_num=hit_by_anyone(rx,ry,r_d,ROODOLF,temp_num)
            if rx == - 100 : 
                santa_map[r_x][r_y] = 0
                break
            if in_range(rx,ry) :
                santa_appa[temp_num] = rounds+2
                if santa_map[rx][ry] == 0  : 
                    santa_map[rx][ry] = temp_num
                    santa_map[r_x][r_y] = 0
                    break
                elif santa_map[rx][ry] != 0 : 

                    continue
            else : # 밖으로 나가거나 하는경우 
                break

    return 


def hit_by_anyone(x,y,direct,WHO,before_num): # 그다음에 갈곳에 산타가 존재하는걸 찾는거야.
    if santa_map[x][y] != 0 : #기존에 존재해!!  그러면 넣어야 할 산타번호를 빼주고 그다음 녀석을 또 추적하라고 빼줘야함.
        temp_num = santa_map[x][y]
        if WHO == ROODOLF:
            nx,ny = x+c*rdx[direct],y+c*rdy[direct]
            if in_range(nx,ny) : 
                santa_map[x][y] = before_num
                return nx,ny,temp_num
            else : 
                return -100,-100,_
        if WHO == SANTA:
            nx,ny = x+dx[direct],y+dy[direct]
            if in_range(nx,ny) : 
                santa_map[x][y] = before_num
                return nx,ny,temp_num
            else : 
                return -100,-100,_
    else : #존재하지않으면 그냥 패스 
        santa_map[x][y] = before_num
        return -100,-100,_



def is_santa_all_die():
    for i in range(n) : 
        for j in range(n) : 
            if santa_map[i][j] != 0 : 
                return False
    return True

def is_santa_appa(santa_num,rounds):
    return santa_appa[santa_num] > rounds

def santan_moveTo_roodolf(sx,sy,rx,ry):

    short_distance = cal_distance(rx,ry,sx,sy)
    next_direction = -1
    x,y = sx,sy
    for num in range(4):
        nx,ny = x+dx[num],y+dy[num]
        if in_range(nx,ny) and santa_map[nx][ny] == 0 : 
            distance = cal_distance(nx,ny,rx,ry)
            if distance < short_distance:
                short_distance = distance
                next_direction = num

    next_x,next_y= sx+dx[next_direction],sy+dy[next_direction]
    if next_direction == -1 : #움직일수있는곳이 없으면 그대로 가만히
        return sx,sy,next_direction
    return next_x,next_y,next_direction

def attack_by_santa(sx,sy,sd,santa_num):
    nd = (sd+2)%4 #반대편방향으로 

    nx,ny = sx+d*dx[nd],sy+d*dy[nd]
    if not in_range(nx,ny): # 밖으로나갔으면 
        return -1,-1 # out 처리 

    return nx,ny


def santa_millim(temp_arr,x,y,md):
    #temp에 있는애를 밀어야함.
    #그리고 그 temp가 또 해당되는지 봐야함.
    gizon_zari = temp_arr[x][y] # 얘가 뒤로 날아갈놈. 
    minunnom = santa_map[x][y]
    nx,ny = x+dx[md],y+dy[md]
    temp_arr[x][y] = 0 
    if in_range(nx,ny):
        temp_arr[nx][ny] = gizon_zari
        santa_map[nx][ny] = gizon_zari
        return temp_arr,nx,ny
    else : 
        return temp_arr,x,y
    
def one_santa_move(santa_num):  #얘를, 루돌프랑, 산타 어택일때로 나눠놨어야했는데...
    global r_x,r_y
    for i in range(n):
        for j in range(n):
            if santa_map[i][j] == santa_num:
                if not is_santa_appa(santa_num,rounds) :

                    nx,ny,nd = santan_moveTo_roodolf(i,j,r_x,r_y)
                    santa_direction[santa_num] = nd
                    santa_map[i][j] = 0
                    santa_map[nx][ny] = santa_num

                    if nx == r_x and ny == r_y : # 루돌프와 충돌한다면 
                        santa_map[nx][ny] = 0
    
                        ax,ay = attack_by_santa(nx,ny,nd,santa_num) # 충돌하고 난 다음 포인트 적립, 반대방향으로 밀려남 
                        if ax == -1 and ay == -1 :  # 그냥 밖으로 나가버리면 끝 
                            santa_point[santa_num] += d 
                            return
                        temp_num = santa_num
                        santa_appa[santa_num] = rounds+2
                        santa_point[santa_num] += d 
                        nd = (nd+2)%4
                        # 산타 충돌체크 
                        if santa_map[ax][ay] != 0 :
                            while True : # 산타가있다면?
                                ax,ay,temp_num=hit_by_anyone(ax,ay,nd,SANTA,temp_num)
                                if ax == -100: break
                                santa_map[ax][ay] = temp_num
                                if in_range(ax,ay) :
                                    if santa_map[ax][ay] == 0  : 
                                        santa_map[ax][ay] = temp_num
                                        break
                                    elif santa_map[ax][ay] != 0 : 
                                        continue
                                else : # 밖으로 나가거나 하는경우 
                                    break
                        else : #0이라면 
                            santa_map[ax][ay] = santa_num
                        
                    return
def santa_move(rounds,rx,ry) :
    #한번 map 위에있는놈으로 해보자, 시간초과나면 배열로 다시 빼기 -100,-100으로 
    for santa_num in range(1,p+1):
        one_santa_move(santa_num)

    return

def santa_point_up():
    for i in range(n) : 
        for j in range(n) : 
            if santa_map[i][j] != 0 : 
                santa_num = santa_map[i][j]
                santa_point[santa_num] += 1 
    return

for rounds in range(1,m+1):
    roodolf_move()
    if is_santa_all_die(): break
    santa_move(rounds,r_x,r_y)
    if is_santa_all_die(): break
    santa_point_up()

for k in range(1,p+1):
    print(santa_point[k],end=' ')