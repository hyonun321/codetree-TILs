#import sys
#sys.stdin = open('루돌프의 반란2.txt','r')



# 1. 두칸 사이의 거리를 구하는 함수
# 2. 산타와 루돌프는 2차원배열로 관리
# 3. bfs로 최단경로를 구하는거다.
# 4. dx,dy 테크닉
# 5. 2차원배열 산타, 2차원배열 루돌프 + @ (산타의 위치 arr)
# 6. 산타 기절조건 배열

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]

POINT =4
n,m,p1,c,d = map(int,input().split())
board = [ [ 0 for _ in range(n)] for _ in range(n)]
santa_arr = [[0,0,0,0,0]] # 1.번호, 2.x, 3.y, 4.움직일수있는턴, 5.산타점수
rx,ry = map(int,input().split())
rx-=1
ry-=1
board[rx][ry] = 50
for _ in range(p1) : 
    p,sr,sc = map(int,input().split())
    sr-=1
    sc-=1
    board[sr][sc] = p
    santa_arr.append([p,sr,sc,0,0])
santa_arr.sort(key=lambda x:x[0])

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def cal_dist(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2

def roo_move():
    global rx,ry
    l_dist = 10000
    nnx,nny = -1,-1
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if 1 <= board[i][j] <= 30 :     
                dist = cal_dist(rx,ry,i,j)
                if l_dist > dist:
                    l_dist = dist
                    nnx,nny = i,j
    #print(nnx,nny)
    # 가까워지는 방향으로 한칸 돌진 
    rd = -1
    for num in range(8):
        nx,ny = rx+dx[num],ry+dy[num]
        if in_range(nx,ny) :
            ddist = cal_dist(nnx,nny,nx,ny)
            if l_dist> ddist : 
                rrx,rry=nx,ny
                l_dist = ddist
                rd = num
    #print(rrx,rry)
    board[rx][ry] = 0
    if 1 <= board[rrx][rry] <= 30 : # 이동할 자리에 산타가 있으면 
        p_santa = board[rrx][rry]
        santa_arr[p_santa][POINT] += c 
        santa_arr[p_santa][3] = rounds+2
        ttd = rd 
        nx,ny = rrx+c*dx[rd],rry+c*dy[rd] # 그다음 날려. 
        if in_range(nx,ny): 
            ttx,tty = nx,ny
            ttnum = p_santa
            while True : 
                if not is_santa(ttx,tty) : break
                ttx,tty,ttd,ttnum = continous_santa_push(ttx,tty,ttd,ttnum)
            if in_range(ttx,tty) and  not is_santa(ttx,tty):
                board[ttx][tty] = ttnum
                santa_arr[ttnum][1] = ttx
                santa_arr[ttnum][2] = tty
        else : #밖으로 나간경우 탈락시켜야함. 
            santa_arr[p_santa][1]=-100
            santa_arr[p_santa][2]=-100
    board[rrx][rry] = 50 # 덮어 올려버려
    rx,ry = rrx,rry

    return

def san_move(idx):
    sx,sy = santa_arr[idx][1],santa_arr[idx][2]
    b_dist = cal_dist(rx,ry,sx,sy)
    nnx,nny = -1,-1
    trigger = False
    for num in range(0,8,2):
        nx,ny = sx+dx[num],sy+dy[num]
        if in_range(nx,ny) and board[nx][ny] == 0 : 
            dist = cal_dist(rx,ry,nx,ny)
            if b_dist > dist : 
                b_dist = dist
                nnx,nny = nx,ny
        elif in_range(nx,ny) and board[nx][ny] == 50 : #루돌프다?
            trigger = True
            rd = num
            nnx,nny = nx,ny
            break
    
    if nnx == -1 and nny == -1: 
        nnx,nny = sx,sy
    else :
        santa_arr[idx][1] = nnx
        santa_arr[idx][2] = nny

    if trigger : # 산타가 이동하다가 루돌프에 부딫혔다. 
        rd = (rd+4)%8
        td = rd
        tnum = idx
        board[sx][sy] = 0
        santa_arr[idx][POINT] += d
        santa_arr[idx][3] = rounds+2
        #print(nnx,nny)
        tx,ty = nnx+d*dx[rd],nny+d*dy[rd]
        if in_range(tx,ty):
            nnx,nny = tx,ty
            while True : 
                if not is_santa(tx,ty):break
                tx,ty,td,tnum =continous_santa_push(tx,ty,td,tnum)
            board[tx][ty] = tnum
            santa_arr[tnum][1]=tx
            santa_arr[tnum][2]=ty
            
        else : # 밖으로 나갈때 
            santa_arr[idx][1]=-100
            santa_arr[idx][2]=-100
            board[sx][sy] = 0
        # 정상적으로 나온놈 이제 백업해줘야함. 
        

    else :
        board[sx][sy] = 0
        board[nnx][nny] = santa_arr[idx][0] # 첫산타가 최종적으로 움직이는곳이 nnx,nny 
 
    #산타가 이동했는데 이때 루돌프가 있으면 연쇄 충돌작용필요. 

    return

def is_santa(tx,ty):
    if in_range(tx,ty) and 1 <= board[tx][ty] <= 30: 
        return True
    else : 
        return False

def continous_santa_push(x,y,d,num):
    nd = d
    if not in_range(x,y): return x,y,d,num
    nnum = board[x][y]
    board[x][y] = num
    santa_arr[num][1] = x
    santa_arr[num][2] = y 
    nx,ny = x+dx[d],y+dy[d]
    if in_range(nx,ny):
        return nx,ny,nd,nnum
    else : 
        santa_arr[nnum][1] = -100
        santa_arr[nnum][2] = -100
        return nx,ny,nd,nnum



def santa_point_up():
    for num in range(1,p1+1):
        if santa_arr[num][1] == -100 : continue
        santa_arr[num][POINT] += 1
    return

def santa_shock():
    return

for rounds in range(m):
    roo_move()

    for idx in range(1,p1+1):
        if santa_arr[idx][3] <= rounds and santa_arr[idx][1] != -100 : 
            san_move(idx)
    santa_point_up()

for kxx in range(1,p1+1):
    print(santa_arr[kxx][POINT],end=' ')