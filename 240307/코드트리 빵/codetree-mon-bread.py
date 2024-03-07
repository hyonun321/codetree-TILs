import sys
from collections import deque
#sys.stdin=open('코드트리빵.txt','r')
dx=[-1,0,0,1]
dy=[0,-1,1,0]

n,m = map(int,input().split())
combini=[0]
maps= [ list(map(int,input().split())) for _ in range(n)] # basecamp
combini_map = [ [ 0 for _ in range(n)] for _ in range(n)]
for first in range(m) : 
    xx,yy = map(int,input().split())
    xx-=1
    yy-=1
    combini.append((xx,yy))
    combini_map[xx][yy] = first+1

people_now = [ (-1,-1)for _ in range(31)]

def find_way_combini(sx,sy,fx,fy):
    distance = 0
    queue = deque()
    queue.append((sx,sy,distance))
    visited = [ [-1 for _ in range(n)] for _ in range(n)]
    visited[sx][sy] = distance
    come = [ [ 0 for _ in range(n)] for _ in range(n)]
    while queue:
        x,y,dd = queue.popleft()
        distance +=1
        if x == fx and y == fy : break
        for num in range(4):
            nx,ny = x+dx[num],y+dy[num]
            if in_range(nx,ny) and visited[nx][ny] == -1 and is_basecamp_ok(nx,ny) and is_combini_ok(nx,ny) : 
                queue.append((nx,ny,dd))
                come[nx][ny] = (x,y)
                visited[nx][ny] = visited[x][y] + 1
    rx=fx
    ry=fy
    while not (rx == sx and ry == sy ) : 
        nx,ny = come[rx][ry]
        if nx == sx and ny == sy : break
        rx,ry = nx,ny
    next_x,next_y = rx,ry
    return next_x,next_y 


def peoples_walk():
    for people in range(len(people_now)) : 
        if people == 0 : continue
        else : 
            #진행하면됨
            a,b = people_now[people]
            if a==-1 and b == -1 : continue
            ca,cb = combini[people]
            next_x,next_y = find_way_combini(a,b,ca,cb)
            people_now[people] = next_x,next_y



    return
def combini_check():

    for people in range(len(people_now)) : 
        if people == 0 : continue
        a,b = people_now[people]
        if a==-1 and b == -1 : continue
        if combini_map[a][b] == people : 
            combini_map[a][b] = -1


    return
def in_range(x,y):
    return 0<=x<n and 0<=y<n

def is_basecamp_ok(x,y):
    return maps[x][y] != -1

def is_combini_ok(x,y):
    return combini_map[x][y] != -1

def base_camp_find(sx,sy,fx,fy):
    distance = 0
    queue = deque()
    queue.append((sx,sy,distance))
    visited = [ [-1 for _ in range(n)] for _ in range(n)]
    visited[sx][sy] = distance
    while queue:
        x,y,dd = queue.popleft()
        distance +=1
        if x == fx and y == fy : break
        for num in range(4):
            nx,ny = x+dx[num],y+dy[num]
            if in_range(nx,ny) and visited[nx][ny] == -1 and is_basecamp_ok(nx,ny) and is_combini_ok(nx,ny) : 
                queue.append((nx,ny,dd))
                visited[nx][ny] = visited[x][y] + 1
                
    return visited[fx][fy]

def people_upload(round):
    if round <= m : 
        #가고싶은 편의점과 가장 가까운 베이스캠프로 들어감.
        combini_x,combini_y = combini[round]
        min_distance = 1e9
        min_x,min_y= -1,-1
        for i in range(n):
            for j in range(n) : 
                if maps[i][j] == 1 :
                    distance = base_camp_find(i,j,combini_x,combini_y)
                    if distance == -1 : continue
                    if min_distance > distance:
                        min_distance = distance
                        min_x,min_y = i,j
        people_now[round] = (min_x,min_y)
        maps[min_x][min_y] = -1
    return

def is_all_people_moved():
    for i in range(len(combini)):
        if i == 0 : continue
        a,b = combini[i]
        if combini_map[a][b] > 0 :
            return False
    return True

round = 0
while True :
    round += 1 
    peoples_walk()
    combini_check()
    people_upload(round)
    if is_all_people_moved() : break
print(round)