import sys
from collections import deque
import time
start_time = time.time()
#sys.stdin = open('자율주행전기차.txt','r')
deb =2
n,m,battery = map(int,input().split())
maps = []
for _ in range(n) :
    tm = list(map(int,input().split()))
    maps.append(tm)
car_x,car_y = map(int,input().split())
car_x -=1
car_y -=1
d_arr = []
for i in range(m) :
    x_s,y_s,x_e,y_e = map(int,input().split())
    maps[x_s-1][y_s-1]= i+11
    d_arr.append((i+501,x_e-1,y_e-1))
dx=[-1,0,1,0]
dy=[0,-1,0,1]

def in_range(x,y) :
    return 0<=x<n and 0<=y<n

def check_short_customer(battery):
    bt_chk = True
    min_ways = 10000000
    c_x,c_y = -1,-1
    min_num= -1
    for i in range(n) :
        for j in range(n) :
            if maps[i][j] >10 and maps[i][j] < 500 :
                c_num = maps[i][j]
                way_arr,all_way = find_custsomer(i,j,battery)
                if all_way == -1 :
                    return 0,0,0,0,False
                if all_way < min_ways:
                    min_num = c_num
                    min_ways = all_way
                    c_x,c_y = i,j

    if battery - min_ways <= 0  :
        bt_chk= False
    return min_num,c_x,c_y,min_ways,bt_chk

def find_custsomer(a,b,battery):

    all_ways = 0
    ways_arr = []
    x1,y1 = car_x,car_y
    queue = deque()
    queue.append((x1,y1))
    visited= [ [False for _ in range(n)] for _ in range(n)]
    visited[x1][y1]=True
    come = [ [0  for _ in range(n)] for _ in range(n)]

    while queue:
        possible = True
        x,y = queue.popleft()
        for num in range(4):
            nx,ny = x+dx[num],y+dy[num]
            if in_range(nx,ny) and visited[nx][ny] == False and maps[nx][ny] != 1 :
                visited[nx][ny] = True
                queue.append((nx,ny))
                come[nx][ny] = (x,y)
                if nx == a and ny == b :
                    possible = False
        if possible == False:
            break
    if visited[a][b] == False:
        return [],-1
    if deb == 1 :
        for c in visited:
            print(*c)
        for c in come:
            print(*c)
    aa,bb = a,b
    while aa != x1 or bb != y1 :
        all_ways+=1
        ways_arr.append((aa,bb))
        aa,bb = come[aa][bb]

    return ways_arr,all_ways

def check_short_destination(battery,c_number):
    bt_chk = True
    d_number = c_number + 490
    d_x,d_y = -1,-1
    for item in d_arr:
        k,i,j = item
        if k == d_number:
            ways_arr,all_ways = find_custsomer(i, j, battery)
            if all_ways == -1:
                return 0, 0, 0, False
            d_x,d_y = i,j
    if battery - all_ways < 0  :
        bt_chk= False
    return  d_x,d_y,all_ways,bt_chk
count = 0
while True:
    min_ways = 1000000
    min_c_number = -1
    c_number,c_x,c_y,c_ways,bt_chk = check_short_customer(battery)
    if bt_chk == False:
        print(-1)
        break
    else :
        maps[c_x][c_y] = 0
        battery -= c_ways
        car_x, car_y = c_x, c_y
    #print(c_number,c_x,c_y,c_ways,bt_chk,battery)
    ##이제 최단거리로 경로로 옮겨줘야함.
    d_x,d_y,d_ways,bt_chk = check_short_destination(battery,c_number)
    if bt_chk == False:
        print(-1)
        break
    else :
        battery += d_ways
        count += 1
        car_x, car_y = d_x, d_y
    #print(d_x,d_y,d_ways,bt_chk)
    if count == m :
        print(battery)
        break


end = time.time()
# print(start_time)
# print(end)