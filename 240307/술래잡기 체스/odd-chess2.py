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
    a,b,c,d,e,f,g,h= map(int,input().split())
    number_arr[a] =(tt,0)
    maps[tt][0]=(a,b-1)

    number_arr[c] =(tt,1)
    maps[tt][1]=(c,d-1)

    number_arr[e] =(tt,2)
    maps[tt][2]=(e,f-1)

    number_arr[g] =(tt,3)
    maps[tt][3]=(g,h-1)

def catch_horse(mx,my):
    catch_number,master_direcition =maps[mx][my]
    number_arr[catch_number] = (-1,-1)
    maps[mx][my] = (-1,-1)
    return catch_number,master_direcition
def move_horse():
    # maps 를 쭉 읽어오다가 문제가 생기니까 1~16 위치를 배열에 담아서 가져오게 해야함.
    for number in range(1,17):
        a,b = number_arr[number]
        if a == -1 and b == -1 : continue
        one_move(a,b)
    return

def one_move(x,y):
    a,b = maps[x][y]
    d = b
    nx,ny = x+dx[d],y+dy[d]
    if in_range(nx,ny) and not (maps[nx][ny] == (-1,-1)):
        #이거바꿀때 바꾸는놈 배열위치값도 반영해줘야함.
        t_number,t2 = maps[x][y]
        t2_number,t4 = maps[nx][ny]

        number_arr[t2_number] = (x,y)
        maps[x][y] = t2_number,t4

        number_arr[t_number] = (nx,ny)
        maps[nx][ny] = t_number,t2
    else : 
        d = (d+1)%8
        maps[x][y] = (a,d)
        one_move(x,y)
    return

def done(x,y,d):
    for dist in range(1,5):
        nx,ny=x+dx[d]*dist,y+dy[d]*dist
        if in_range(nx,ny) and maps[nx][ny] != (0,0):
            return False
    return True

def search_max_score(x,y,d,score):
    global max_score
    if done(x,y,d):
        max_score = max(max_score,score)
        return 
    
    for dist in range(1,5):
        nx,ny=x+dx[d]*dist,y+dy[d]*dist

        if not (in_range(nx,ny) and maps[nx][ny] != (0,0)): continue
        temp = [[maps[i][j] for j in range(n)]for i in range(n)]

        second_score,second_dir = catch_horse(nx,ny)
        maps[x][y] = (0,0) # 빈칸처리
        move_horse()
        search_max_score(x,y,second_dir,second_score+score)
        
        for i in range(n):
            for j in range(n):
                maps[i][j] = temp[i][j]



max_score = 0
first_score,first_dir = catch_horse(mx,my)
move_horse()
search_max_score(mx,my,first_dir,first_score)
print(max_score)