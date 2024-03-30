import sys

#sys.stdin=open('술래잡기.txt','r')

dx=[-1,0,1,0]
dy=[0,1,0,-1]
run_arr = []

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def cal_dist(runner):
    rx,ry,rd = run_arr[runner]
    return abs(cx-rx)+abs(cy-ry)

n,m,h,k = map(int,input().split())
tree_arr = [ [False for _ in range(n)] for _ in range(n)]
for number in range(m):
    x1,y1,d1 = map(int,input().split())
    x1-=1
    y1-=1
    run_arr.append((x1,y1,d1))
for tree in range(h):
    tx1,ty1 = map(int,input().split())
    tx1-=1
    ty1-=1
    tree_arr[tx1][ty1] = True

cx,cy = n//2,n//2
cd = 0

def one_runner_move(number):

    rx,ry,rd = run_arr[number]

    if cal_dist(number) <= 3 : # 술래와 거리가 3이하만 움직인다.
        nx,ny = rx+dx[rd],ry+dy[rd]
        if in_range(nx,ny):
            if cx==nx and cy == cy : #안움직인다.
                return
            else : # 술래가 없다면
                run_arr[number] = nx,ny,rd
        else : #가려는방향이 벗어났다면
            rd = (rd+2)%4
            nnx,nny = rx+dx[rd],ry+dy[rd]
            if nnx == cx and nny == cy :
                return
            else : # 술래가없다면
                run_arr[number] = nnx,nny,rd
        return


def all_runner_move():
    for number in range(m):
        one_runner_move(number)
    return

visited = [ [False for _ in range(n)] for _ in range(n)]
def catch_move():
    global  cx,cy,cd,catch_forward,visited
    if catch_forward: # n//2,n//2 에서 0,0까지
        # 0,0일때랑, n//2,n//2 일때 처리를 해줘야해.
        if cx== n//2 and cy == n//2 :
            visited[cx][cy] = True
            cx,cy = cx+dx[cd],cy+dy[cd]
            visited[cx][cy] = True
            cd = (cd+1)%4
            return
        #나머지들은?
        ncd = (cd + 1)%4
        #그다음 향할 방향이
        ncx,ncy = cx+dx[ncd],cy+dy[ncd]
        if in_range(ncx,ncy) and visited[ncx][ncy] == True:
            cx,cy = cx+dx[cd],cy+dy[cd] # 한칸 이동하고 바로 돌려야해
            visited[cx][cy] = True
            #이동한거야.
            if cx == 0 and cy == 0 : #어라?
                cd = 2
                catch_forward = False
                visited = [ [False for _ in range(n)] for _ in range(n)]
            else :
                ncx, ncy = cx + dx[ncd], cy + dy[ncd]
                if in_range(ncx,ncy) and visited[ncx][ncy] == False:
                    cd = (cd +1)%4
        else : #방문한적이 없어
            pass

    else : #0,0에서 n//2,n//2까지
        if cx== 0 and cy == 0 :
            visited[cx][cy] = True
            cx,cy = cx+dx[cd],cy+dy[cd]
            visited[cx][cy] = True
            return
        #나머지들은?
        ncx,ncy = cx+dx[cd],cy+dy[cd]
        if in_range(ncx,ncy) :
            if visited[ncx][ncy] :
                cd = (cd-1)%4
            else :
                cx,cy = cx+dx[cd],cy+dy[cd] # 한칸 이동하고 바로 돌려야해
                visited[cx][cy] = True
                ncx, ncy = cx + dx[cd], cy + dy[cd]
                if in_range(ncx,ncy) and visited[ncx][ncy] == False:
                    pass
                else :
                    cd = (cd -1)%4
            #이동한거야.
            if cx == n//2 and cy == n//2 : #어라?
                cd = 0
                catch_forward = True
                visited = [[False for _ in range(n)] for _ in range(n)]
        else :pass


    return

def catch_look(rounds):
    count = 0
    for look in range(3):
        nx,ny = cx+look*dx[cd],cy+look*dy[cd]
        # 술래 칸 + 2 까지 도망자를 잡는다.
        for runner in range(m):
            rx,ry,rd = run_arr[runner]
            if rx == -100 : continue
            if rx == nx and ry == ny :
                if tree_arr[rx][ry] : #나무라면
                    continue
                else : # 나무가 False라면?
                    run_arr[runner]= -100,-100,-1
                    count +=1
                    #지옥으로 보낸다.

    return rounds*count
point = 0
catch_forward = True
for rounds in range(1,k+1):
    all_runner_move()
    catch_move()
    point += catch_look(rounds)
print(point)