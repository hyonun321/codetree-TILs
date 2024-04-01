import sys

#sys.stdin =open('나무박멸.txt','r')

n,m,k,c = map(int,input().split())
maps = [ list(map(int,input().split())) for _ in range(n)]

diezone = [ [ 0 for _ in range(n)] for _ in range(n)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<n


def tree_grow():
    for i in range(n):
        for j in range(n):
            if maps[i][j] >0 :
                count = 0
                for num in range(4):
                    nx,ny = i+dx[num],j+dy[num]
                    if in_range(nx,ny) and maps[nx][ny] >0 :
                        count += 1
                maps[i][j] += count
    return

def tree_bunsik(rounds):
    global maps
    tmaps = [ [maps[i][j] for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if maps[i][j] > 0 :
                tpower = maps[i][j]
                count = 0
                grow_arr =[]
                for num in range(4):
                    nx,ny = i+dx[num],j+dy[num]
                    if in_range(nx,ny) and maps[nx][ny] == 0 and diezone[nx][ny] <= rounds :
                        count += 1
                        grow_arr.append((nx,ny))
                for tx,ty in grow_arr:
                    tmaps[tx][ty] += tpower//count

    maps = [ [tmaps[i][j] for j in range(n) ] for i in range(n) ]
    return

rdx=[-1,-1,1,1]
rdy=[1,-1,-1,1]
def zecho_act(x,y):
    point = 0
    point += maps[x][y]
    die_direction = []
    zecho_arr = [(x,y)]
    for power in range(1,k+1):
        for num in range(4):
            if num in die_direction: continue
            nx,ny = x+power*rdx[num],y+power*rdy[num]
            # 벽 or 나무가 아예 없으면 그칸까지는 제초제 뿌린다.
            if in_range(nx,ny) and maps[nx][ny] >0 :
                point += maps[nx][ny]
                zecho_arr.append((nx,ny))
            elif in_range(nx,ny) and (maps[nx][ny] == -1 or maps[nx][ny] == 0):
                point += maps[nx][ny]
                zecho_arr.append((nx,ny))
                die_direction.append(num)
    return point,zecho_arr


def zechoze():
    max_die = 0
    max_arr= []
    mx,my = -1,-1
    for i in range(n):
        for j in range(n):
            if maps[i][j] >0 :
                t_die,t_arr = zecho_act(i,j)
                if t_die > max_die :
                    max_die = t_die
                    max_arr = t_arr
                    mx,my = i,j
    return max_die,mx,my,max_arr

def kill_tree(rounds,mx,my,marr):
    if mx == -1 : return
    #maps[mx][my] = 0
    #diezone[mx][my] = rounds+2

    #for power in range(1,k+1):
    #    for num in range(4):
    #        nx,ny = mx+power*rdx[num],my+power*rdy[num]
    #        if in_range(nx,ny)  :
    #            diezone[nx][ny] = rounds+2
    #            maps[nx][ny] = 0
    for x,y in marr:
        if maps[x][y] == -1 :
            diezone[x][y] = rounds + c
        else :
            maps[x][y] = 0
            diezone[x][y] = rounds + c

    return
answer = 0
for rounds in range(m):
    tree_grow()
    tree_bunsik(rounds)
    c,mx,my,marr = zechoze()
    answer += c
    kill_tree(rounds,mx,my,marr)
print(answer)