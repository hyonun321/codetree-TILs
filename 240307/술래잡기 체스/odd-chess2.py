#import sys
#sys.stdin=open('술래잡기체스.txt','r')

def in_range(x,y):
    return 0<=x<n and 0<=y<n
n =4 
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]
maps = [ [(0,0) for _ in range(4)] for _ in range(4)]
mx,my =0,0
number_arr = [0 for _ in range(17)]
for tt in range(4):
    a2,b2,c2,d2,e,f,g,h= map(int,input().split())
    number_arr[a2] =(tt,0)
    maps[tt][0]=(a2,b2-1)

    number_arr[c2] =(tt,1)
    maps[tt][1]=(c2,d2-1)

    number_arr[e] =(tt,2)
    maps[tt][2]=(e,f-1)

    number_arr[g] =(tt,3)
    maps[tt][3]=(g,h-1)

def catch_horse(mx,my):
    catch_number,master_direcition =maps[mx][my]
    number_arr[catch_number] = (-2,-2) # 현재 술래잡이중이다.
    maps[mx][my] = (-2,-2)
    return catch_number,master_direcition


def move_horse():
    # maps 를 쭉 읽어오다가 문제가 생기니까 1~16 위치를 배열에 담아서 가져오게 해야함.
    for number in range(1,17):
        (ii,jj) = number_arr[number]
        if maps[ii][jj] == (-2,-2) or maps[ii][jj] == (-1,-1) : continue
        one_move(ii,jj)
    return

def thief_can_go(x, y):
    return in_range(x, y) and maps[x][y] != (-2,-2)


# 술래가 이동할 수 있는 곳인지를 판단합니다.
# 격자 안이면서, 도둑말이 있어야만 합니다.
def tagger_can_go(x, y):
    return in_range(x, y) and maps[x][y] != (-1,-1)

def one_move(x,y):
    a,d = maps[x][y]
    for dist in range(8):
        nd = (d+dist)%8
        nx,ny = x+dx[nd],y+dy[nd]
        if thief_can_go(nx,ny):
            #이거바꿀때 바꾸는놈 배열위치값도 반영해줘야함.

            t_number,t2 = a,nd
            t2_number,t4 = maps[nx][ny]

            number_arr[t2_number] = (x,y)
            maps[x][y] = t2_number,t4

            number_arr[t_number] = (nx,ny)
            maps[nx][ny] = t_number,t2
            
            return

    return

def done(x,y,d):
    for dist in range(1,5):
        nx,ny=x+dx[d]*dist,y+dy[d]*dist
        if tagger_can_go(nx,ny):
            return False
    return True

def search_max_score(x,y,d,score):
    global max_score
    if done(x,y,d):
        max_score = max(max_score,score)
        return 
    
    for dist in range(1,5):
        nx,ny=x+dx[d]*dist,y+dy[d]*dist

        if not tagger_can_go(nx,ny): continue
        temp = [[maps[i][j] for j in range(n)]for i in range(n)]

        second_score,second_dir = catch_horse(nx,ny)
        maps[x][y] = (-1,-1) # 빈칸처리
        maps[nx][ny] = (-2,-2) # 말처리 velog 기입하기. 
        move_horse()
        search_max_score(nx,ny,second_dir,second_score+score)
        
        for i in range(n):
            for j in range(n):
                maps[i][j] = temp[i][j]



max_score = 0
first_score,first_dir = catch_horse(mx,my)
move_horse()
search_max_score(mx,my,first_dir,first_score)
print(max_score)