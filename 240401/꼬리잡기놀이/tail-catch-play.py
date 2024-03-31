import sys
from collections import deque
#sys.stdin = open('꼬리잡기놀이.txt','r')

head=[]
n,m,k = map(int,input().split())
maps = []
people_arr = [ 0 for _ in range(m)]
master_visited = [ [False for _ in range(n)] for _ in range(n) ]

for i in range(n):
    tarr = list(map(int,input().split()))
    for j in range(n):
        item = tarr[j]
        if item == 1 :
            head.append((i,j))
            master_visited[i][j]=True
        elif item == 2 :
            master_visited[i][j] = True
        elif item == 3 :
            master_visited[i][j] = True
        elif item == 4 :
            tarr[j] = 0
            master_visited[i][j] = True
        else :
            tarr[j] = -1
    maps.append(tarr)

def in_range(x,y):
    return 0<=x<n and 0<=y<n

dx=[-1,0,1,0]
dy=[0,1,0,-1]




def move_all():
    global maps
    # 경로를 arr에 넣고.
    # 새로운 경로를 append 하고,
    # 나머지는 popleft 해서 빼주고
    # 그 어레이를 임시배열에 반영하고
    # 업데이트하면 끝.
    tmaps = [ [-1 for _ in range(n)] for _ in range(n)]
    for t1 in range(len(head)):
        gx,gy = head[t1]
        g_arr =deque()
        g_arr.append((gx,gy))
        queue = deque()
        visited=[ [False for _ in range(n)] for _ in range(n)]
        queue.append((gx,gy))
        visited[gx][gy] = True
        while queue:
            x,y = queue.popleft()
            for num in range(4):
                nx,ny = x+dx[num],y+dy[num]
                if in_range(nx,ny) and visited[nx][ny] == False and (maps[nx][ny] >= 2)  :
                    if x == gx and y == gy and maps[nx][ny] >= 3 : continue
                    queue.append((nx,ny))
                    visited[nx][ny] = True
                    g_arr.append((nx,ny))
        #print(g_arr)
        #print(visited)
        # 이제 머리가 그다음 한칸을 이동한다.

        for num in range(4):
            nx,ny = gx+dx[num],gy+dy[num]
            if in_range(nx,ny) and (maps[nx][ny] == 0 or maps[nx][ny] == 3 or maps[nx][ny] == len(g_arr)) :
                # 갈수있어!
                g_arr.appendleft((nx,ny))
                break
        g_arr.pop() # 머리값 뺀다.
        # g_arr에 있는걸 tmaps 에 적용시킵니다.
        head[t1] = g_arr[0]
        people_arr[t1] = g_arr
        for tt in range(len(g_arr)):
            xx,yy = g_arr[tt]
            tmaps[xx][yy] = tt+1
        #print(tmaps)


    for i in range(n):
        for j in range(n):
            if master_visited[i][j] == True:
                maps[i][j] = 0
                if 1 <= tmaps[i][j] :
                    maps[i][j] = tmaps[i][j]
    #print(maps)


    return

def heat_change(x,y):
    for number in range(len(people_arr)):
        arr = people_arr[number]
        if (x,y) in arr :
            # 만약 있다면 , 그녀석 방향바꾸기
            arr.reverse()
            head[number] = arr[0]
            #뒤집고 다시 그녀석들 숫자 반영해야함.
            for tt in range(len(arr)):
                xx, yy = arr[tt]
                maps[xx][yy] = tt + 1
    return

def shot(sx,sy,sd):
    global m_point
    for i in range(n):
        nx,ny = sx+i*dx[sd],sy+i*dy[sd]
        if maps[nx][ny] >= 1 :
            m_point += maps[nx][ny]**2
            heat_change(nx,ny)
            break

    return


def shoot_ball(rounds):
    #sd 는 0 상 1 우 2 하 3 좌
    rounds = (rounds)% (4*n)
    if rounds <= n  :
        sx = rounds -1
        sy = 0
        shot(sx,sy,1)
    elif n+1 <= rounds <= 2*n:
        sx = n-1
        sy = rounds -n -1
        shot(sx,sy,0)
    elif 2*n+1<=rounds <= 3*n :
        sx=n-1 - ( rounds - 2*n + 1)
        sy=n-1
        shot(sx,sy,3)
    elif 3*n +1 <= rounds <= 4*n :
        sx=0
        sy=n-1-( rounds - 2*n + 1)
        shot(sx,sy,2)
    else : pass # 이게걸려?




    return
m_point = 0
for rounds in range(1,k+1):
    move_all()
    shoot_ball(rounds)
print(m_point)