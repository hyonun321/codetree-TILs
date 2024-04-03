import sys
from collections import deque
sys.stdin = open('미로타워디펜스.txt','r')

n,m = map(int,input().split())

maps = [ list(map(int,input().split())) for _ in range(n)]

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def in_range(x,y):

    return 0<=x<n and 0<=y<n


def cal_nasun():
    sx,sy = 0,0
    x,y=sx,sy
    num = 0
    way_arr = []
    visited= [ [False for _ in range(n)] for _ in range(n)]
    visited[sx][sy] = True
    way_arr.append((x,y))
    while not (x == n//2 and y == n//2):
        nx,ny = x+dx[num],y+dy[num]
        if in_range(nx,ny) and visited[nx][ny] == False :
            x,y = nx,ny
            way_arr.append((x,y))
            visited[nx][ny] = True

        else :
            num = (num+1)%4


    way_arr.pop()
    way_arr.reverse()
    return way_arr



def attack(d,p):
    x,y = n//2,n//2
    count = 0
    carr = {}
    for power in range(1,p+1):
        nx,ny = x+power*dx[d],y+power*dy[d]
        if in_range(nx,ny):
            if maps[nx][ny] in carr:
                carr[maps[nx][ny]] += 1
                maps[nx][ny] = 0
            else :
                carr[maps[nx][ny]] = 1
                maps[nx][ny] = 0

    for i in carr.keys():
        count += (i * carr[i])

    return count

def blank_update():
    global maps
    new_arr = deque()
    for x,y in master_way:
        if maps[x][y] > 0 :
            new_arr.append(maps[x][y])

    maps= [ [ 0 for _ in range(n)] for _ in range(n)]

    for tx,ty in master_way:
        if len(new_arr) >= 1 :
            maps[tx][ty] = new_arr.popleft()
    return

def fourtimes_delete():
    count = 0
    while True :
        ck, arr = fourtimes_check()
        if ck == False : break
        count +=delete_four(arr)

        blank_update()
    return count

def delete_four(arr):
    count = 0
    tc = 0
    for tarr in arr:
        for x,y in tarr:
            tc = len(tarr) * maps[x][y]
            maps[x][y] = 0

        count += tc
    return count


def fourtimes_check():
    possible = False
    mnumber = 0
    count = 0
    delete_arr = []
    t_arr = []
    for x,y in master_way:

        number = maps[x][y]
        if number > 0 : # 0은 걸리면안된다.
            if number == mnumber :
                count +=1
                t_arr.append((x,y))
            else :
                mnumber = number
                count = 1
                if len(t_arr) >= 4 : # 4개가 넘어가면 바꾸기 전에 그녀석 저장
                    delete_arr.append(t_arr)
                t_arr=[(x,y)]
        else :
            delete_arr.append(t_arr)

        if count >= 4 :
            possible = True



    return possible,delete_arr


def remake_miro():
    global maps
    new_arr = []
    mnumber = maps[n//2][n//2-1]
    t_arr = []
    m_arr = deque()
    count =0
    for x,y in master_way:
        if mnumber == 0 : break
        number = maps[x][y]
        if number > 0 : # 0은 걸리면안된다.
            if number == mnumber :
                count +=1
            else :
                m_arr.append(count)
                m_arr.append(mnumber)
                mnumber = number
                count = 1
        else :
            m_arr.append(count)
            m_arr.append(mnumber)
            mnumber = 0


    maps= [ [ 0 for _ in range(n)] for _ in range(n)]
    for x,y in master_way:
        if len(m_arr) >0:
            maps[x][y] =m_arr.popleft()
        else :
            break

    return
master_way = []
master_way = cal_nasun()
point = 0
for rounds in range(m):
    sd,sp = map(int,input().split())
    point += attack(sd,sp)
    blank_update()
    point += fourtimes_delete()
    remake_miro()
print(point)