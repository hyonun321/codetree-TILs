import sys
import heapq

#sys.stdin = open('싸움땅.txt','r')
dx=[-1,0,1,0]
dy=[0,1,0,-1]
n,m,k = map(int,input().split())
p_gun = [ 0 for _ in range(m)]
maps = [[ [] for _ in range(n)] for _ in range(n)]
for tt1 in range(n):
    t_map = list(map(int,input().split()))
    for tt2 in range(n):
        item = t_map[tt2]
        heapq.heappush(maps[tt1][tt2],-item)
p_info = []
point = [0 for _ in range(m)]
for numbers in range(m):
    x1,y1,d1,s1 = map(int,input().split())
    x1-=1
    y1-=1
    p_info.append([x1,y1,d1,s1])

def in_range(x,y):
    return 0<=x<n and 0<=y<n
def move_p(number):

    px,py,pd,ps = p_info[number]

    nx,ny = px+dx[pd],py+dy[pd]
    if in_range(nx,ny) :
        p_info[number] = [nx,ny,pd,ps]
    else :
        pd = (pd +2 )%4
        nnx,nny =px+dx[pd],py+dy[pd]
        p_info[number] = [nnx,nny,pd,ps]
    return

def check_player(number):
    px,py,pd,ps = p_info[number]
    for t in range(m):
        if t == number : continue
        tx,ty,td,ts = p_info[t]
        if tx==px and ty == py :
            return t,True
    return number, False


def acquire_gun(number):

    px,py,pd,ps = p_info[number]
    if len(maps[px][py]) == 0 : #총이없다면,
        return
    else : #총이있다면,
        gun = p_gun[number]
        if gun == 0 : #플레이어는 총이없다.
            exit_gun = heapq.heappop(maps[px][py])
            exit_gun = -(exit_gun)
            p_gun[number] = exit_gun
        else : #플레이어는 총이있다.
            exit_gun = heapq.heappop(maps[px][py])
            exit_gun = -(exit_gun)
            if exit_gun > gun : #공격력이 더쌔다면
                heapq.heappush(maps[px][py],-gun) #힙큐에 넣어주고
                p_gun[number] = exit_gun
            else : #아닌경우는 다시넣어야함.
                heapq.heappush(maps[px][py],-exit_gun)

    return

def batte(anum,bnum):

    # 두 유저는 이제 싸워야한다.

    ax,ay,ad,as1 = p_info[anum]
    agun = p_gun[anum]
    bx,by,bd,bs1 = p_info[bnum]
    bgun = p_gun[bnum]
    a_power = agun + as1
    b_power = bgun + bs1
    power_diff = abs(a_power - b_power)
    #서로의 파워비교
    if a_power > b_power:
        point[anum] += power_diff
        return anum,bnum
    elif a_power < b_power:
        point[bnum] += power_diff
        return bnum,anum
    else : #둘이 같을때
        if as1 > bs1 : #a가 이김
            point[anum] += power_diff
            return anum, bnum
        else : # b가이김
            point[bnum] += power_diff
            return bnum, anum

def loser_move(number):
    px,py,pd,ps = p_info[number]

    nx,ny = px+dx[pd],py+dy[pd]
    pgun = p_gun[number]
    heapq.heappush(maps[px][py],-pgun)
    p_gun[number] = 0
    if in_range(nx,ny) :
        p_info[number] = [nx,ny,pd,ps]
    else :
        for num in range(4):
            nnd = (pd +num)%4
            nnx,nny =px+dx[nnd],py+dy[nnd]
            if in_range(nnx,nny):
                #빈칸이 보인다면?
                p_info[number] = [nnx,nny,nnd,ps]
                return
    return

def move_all():

    for num in range(m):
        move_p(num)
        battle_num,possible = check_player(num)
        if possible:
            winner,loser = batte(battle_num,num)
            loser_move(loser)
            acquire_gun(loser)
            acquire_gun(winner)
        else :
            acquire_gun(num)

    return

for rounds in range(k):
    move_all()

for k in range(m):
    print(point[k],end=' ')