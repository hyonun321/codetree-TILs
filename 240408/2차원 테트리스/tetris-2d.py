import sys

#sys.stdin = open('2차원테트리스.txt','r')

insert = [ [0 for _ in range(4)] for _ in range(4)]

red = [ [0 for _ in range(10)] for _ in range(4)]
yellow = [ [0 for _ in range(4)] for _ in range(10)]


def block_insert(bt,bx,by):
    global insert
    insert = [ [0 for _ in range(4)] for _ in range(4)]
    if bt == 1 :
        insert[bx][by] = bt
    elif bt == 2 :
        insert[bx][by] = bt
        insert[bx][by+1] = bt

    else :
        insert[bx][by] = bt
        insert[bx+1][by] = bt

    for i in range(4):
        for j in range(4):
            red[i][j] = 0
            yellow[i][j] = 0
            red[i][j] = insert[i][j]
            yellow[i][j] = insert[i][j]

    return

dx=[-1,0,1,0]
dy=[0,1,0,-1]
RED =1
YELLOW = 0
def r_in_range(x,y):
    return 0<=x<4 and 0<=y<10
def y_in_range(x,y):
    return 0<=x<10 and 0<=y<4
def is_block(color,bt,x,y,maps):
    if bt == 1 :
        if maps[x][y] != 0 : return True
    elif bt == 2 :
        if color == RED:
            if not r_in_range(x,y+1) : return True
        else :
            if not y_in_range(x,y+1) : return True
        if maps[x][y] !=0 or maps[x][y+1] !=0 : return True
    elif bt == 3 :
        if color == YELLOW:
            if not y_in_range(x+1,y) : return True
        else :
            if not r_in_range(x+1,y) : return True
        if maps[x][y] != 0 or maps[x+1][y] != 0 : return True

    return False

def yellow_down(bt,bx,by):
    d = 2
    if bt == 1 :
        nx,ny = bx+dx[d],by+dy[d]
        while True :
            nnx,nny = nx+dx[d],ny+dy[d]
            if not y_in_range(nnx,nny) : break
            if is_block(YELLOW,bt,nnx,nny,yellow) : break
            nx,ny = nnx,nny

        yellow[nx][ny]= bt
    elif bt == 2 :
        nx,ny = bx+dx[d],by+dy[d]
        nx1,ny1 = bx+dx[d],by+1+dy[d]
        while True :
            nnx,nny = nx+dx[d],ny+dy[d]
            nnx1, nny1 = nx1 + dx[d], ny1 + dy[d]
            if not y_in_range(nnx,nny) : break
            if is_block(YELLOW,bt,nnx,nny,yellow) : break
            if not y_in_range(nnx1,nny1) : break
            nx,ny = nnx,nny
            nx1,ny1 = nnx1,nny1
        yellow[nx][ny]= bt
        yellow[nx][ny+1] = bt
    else :
        nx,ny = bx+dx[d],by+dy[d]
        nx1,ny1 = bx+1+dx[d],by+dy[d]
        while True :
            nnx,nny = nx+dx[d],ny+dy[d]
            nnx1, nny1 = nx1 + dx[d], ny1 + dy[d]
            if not y_in_range(nnx,nny) : break
            if is_block(YELLOW,bt,nnx,nny,yellow) : break
            if not y_in_range(nnx1,nny1) : break
            nx,ny = nnx,nny
            nx1,ny1 = nnx1,nny1
        yellow[nx][ny]= bt
        yellow[nx+1][ny] = bt
    return

def red_down(bt,bx,by):
    d = 1
    if bt == 1 :
        nx,ny = bx+dx[d],by+dy[d]
        while True :
            nnx,nny = nx+dx[d],ny+dy[d]
            if not r_in_range(nnx,nny) : break
            if is_block(RED,bt,nnx,nny,red) : break
            nx,ny = nnx,nny

        red[nx][ny]= bt
    elif bt == 2 :
        nx,ny = bx+dx[d],by+dy[d]
        nx1,ny1 = bx+dx[d],by+1+dy[d]
        while True :
            nnx,nny = nx+dx[d],ny+dy[d]
            nnx1, nny1 = nx1 + dx[d], ny1 + dy[d]
            if not r_in_range(nnx,nny) : break
            if is_block(RED,bt,nnx,nny,red) : break
            if not r_in_range(nnx1,nny1) : break
            nx,ny = nnx,nny
            nx1,ny1 = nnx1,nny1
        red[nx][ny]= bt
        red[nx][ny+1] = bt
    else :
        nx,ny = bx+dx[d],by+dy[d]
        nx1,ny1 = bx+1+dx[d],by+dy[d]
        while True :
            nnx,nny = nx+dx[d],ny+dy[d]
            nnx1, nny1 = nx1 + dx[d], ny1 + dy[d]
            if not r_in_range(nnx,nny) : break
            if is_block(RED,bt,nnx,nny,red) : break
            if not r_in_range(nnx1,nny1) : break
            nx,ny = nnx,nny
            nx1,ny1 = nnx1,nny1
        red[nx][ny]= bt
        red[nx+1][ny] = bt
    return

def delete_line():
    count = 0
    # yellow
    t_y = [[ 0 for _ in range(4)] for _ in range(6)]
    delete = []
    for i in range(9,5,-1):
        chk = 0
        for j in range(4):
            if yellow[i][j] >0 :
                chk +=1
        if chk == 4 :
            count +=1
            delete.append(i)
    idx = 5
    for i in range(9,3,-1):
        if i in delete : continue
        for j in range(4):
            t_y[idx][j] = yellow[i][j]
        idx -= 1
    for i in range(9,3,-1):
        for j in range(4):
            yellow[i][j] = t_y[i-4][j]


    # red
    t_r = [[ 0 for _ in range(6)] for _ in range(4)]
    delete1 = []
    for j in range(9,5,-1):
        chk = 0
        for i in range(4):
            if red[i][j] >0 :
                chk +=1
        if chk == 4 :
            count +=1
            delete1.append(j)
    idx = 5
    for j in range(9,3,-1):
        if j in delete1 : continue
        for i in range(4):
            t_r[i][idx] = red[i][j]
        idx -= 1
    for j in range(9,3,-1):
        for i in range(4):
            red[i][j] = t_r[i][j-4]
    return count

def push_line():
    #yellow
    t_y = [[0 for _ in range(4)] for _ in range(4)]
    y_line_chk = []
    for i in range(4,6,1):
        for j in range(4):
            if yellow[i][j] >0 :
                y_line_chk.append(i)
                break
    #이제 y_line에있는 행만큼 밀어야한다.

    a = len(y_line_chk)
    for i in range(6-a,10-a,1):
        for j in range(4):
            t_y[i-(6-a)][j] = yellow[i][j]

    for j1 in range(4):
        for i1 in range(4):
            yellow[i1+ 6][j1 ] = t_y[i1][j1]

    # 임시공간 초기화
    for ti in range(4,6,1):
        for tj in range(4):
            yellow[ti][tj] = 0

    #red
    t_r = [[0 for _ in range(4)] for _ in range(4)]
    r_line_chk = []
    for j in range(4, 6, 1):
        for i in range(4):
            if red[i][j] >0 :
                r_line_chk.append(i)
                break
    #이제 y_line에있는 행만큼 밀어야한다.

    a = len(r_line_chk)
    for j in range(6-a,10-a,1):
        for i in range(4):
            t_r[i][j-(6-a)] = red[i][j]

    for j1 in range(4):
        for i1 in range(4):
            red[i1][j1+6] = t_r[i1][j1]

#임시공간 초기화
    for ti in range(4):
        for tj in range(4,6,1):
            red[ti][tj] = 0


    return
def cal_block():
    count = 0

    # yellow
    for i in range(6,10,1):
        for j in range(4):
            if yellow[i][j] >0 :
                count +=1


    # red
    for j1 in range(6,10,1):
        for i1 in range(4):
            if red[i1][j1] >0 :
                count +=1

    return count
k = int(input())

point = 0
for _ in range(k):
    bt,bx,by = map(int,input().split())
    block_insert(bt,bx,by)
    yellow_down(bt,bx,by)
    red_down(bt,bx,by)
    point += delete_line()
    push_line()

print(point)
print(cal_block())